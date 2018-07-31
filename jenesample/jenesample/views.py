#from django.http import HttpResponse
from django.shortcuts import render
from jeneprocessor.jenepdf import JenePDF
from django.views.generic import TemplateView

def render_jene(request):
    pdf_config = JenePDF("test_template.html", "result.pdf")
    result = pdf_config.produce_pdf()
    return result


class SampleClassView(TemplateView):
    def __init__(self):
        self._pdf_config = JenePDF("test_template_context.html", "result_context.pdf")
    
    def get(self, request):
        firstname = "John"
        lastname = "Doe"
        result = self._pdf_config.produce_pdf({'FirstName': firstname, 'LastName': lastname})
        return result
