from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from core.jene_engine import engine


class JenePDF:

    def __init__(self, template_file, filename:str):
        self._response = HttpResponse(content_type='application/pdf')
        self._response["Content-Disposition"] = 'attachment; filename={}'.format(filename) 
        try:
            self._template = get_template(template_file)
        except Exception as exc:
            raise Exception("Error occured during template loading {}".format(exc))
    
    def produce_pdf(self, content:dict={}) -> HttpResponse:
        try:
            engine.response = self._response
            engine.html = self._template.render(content)
            engine.process()
            return engine.response
        except Exception as exc:
            return HttpResponse('Error during pdf generation: {}'.format(exc))