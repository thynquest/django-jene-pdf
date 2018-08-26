import os
from typing import Callable
from django.http import HttpResponse
from django.conf import settings
from xhtml2pdf import pisa


class _Jene_Engine:
    def __init__(self, html:str, response:HttpResponse):
        self._html = html
        self._response = response
    
    @property
    def html(self) -> str:
        return self._html

    @html.setter
    def html(self, html):
        self._html = html

    @property
    def response(self) -> HttpResponse:
        return self._response

    @response.setter
    def response(self, response:HttpResponse):
        self._response = response
    
    def _process_resources(self, uri, rel):
        # use short variable names
        
        sUrl = settings.STATIC_URL      # Typically /static/
        sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
        sFileDirs = settings.STATICFILES_DIRS    # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL       # Typically /static/media/
        mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/
        path = None

        if uri.startswith(mUrl) and mUrl:
            path = os.path.join(mRoot, uri.replace(mUrl, ""))

        elif uri.startswith(sUrl) and sUrl:
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        
        if not os.path.isfile(path):
            for s in sFileDirs:
                path = os.path.join(s, uri.replace(sUrl, ""))
                if os.path.isfile(path):
                    break
        else:
            raise Exception("Resource(s) not found in {}: check the uri starts with {} or {} ".format(path, sUrl, mUrl))
        
        return path


    def process(self, func_callback: Callable[[str, str], str]=None):
        try:
            if func_callback is None:
                pisaStatus = pisa.CreatePDF(self._html, dest=self._response, 
                                            link_callback=self._process_resources)
                return pisaStatus
            return pisa.CreatePDF(self._html, dest=self._response, link_callback=func_callback)
        except Exception as exc:
            raise Exception("Error during pdf process: {}".format(exc))
    
engine = _Jene_Engine(None, None)

__all__ = ['engine']