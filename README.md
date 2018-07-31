# Django jene pdf


django jene pdf is a simple open source project designed to generate pdf from django template using xhtml2pdf. it is also able to handle context throught a dictionary that will be passed to the jene engine, including the use of settings variable such as STATICFILES_DIRS or STATIC_URL.

## Installation
:zap: pip3 install django-jene-pdf :zap:

## Example

```python
#function based view
from jeneprocessor.jenepdf import JenePDF

def render_jene(request):
    pdf_config = JenePDF("test_template.html", "result.pdf")
    result = pdf_config.produce_pdf()
    return result
```

```python
#class based view
from jeneprocessor.jenepdf import JenePDF
from django.views.generic import TemplateView

class SampleClassView(TemplateView):
    def __init__(self):
        self._pdf_config = JenePDF("test_template_context.html", "result_context.pdf")
    
    def get(self, request):
        firstname = "John"
        lastname = "Doe"
        result = self._pdf_config.produce_pdf({'FirstName': firstname, 'LastName': lastname})
        return result
```
the html file must be in the templates folder of your django project (see jenesample directory for example)
