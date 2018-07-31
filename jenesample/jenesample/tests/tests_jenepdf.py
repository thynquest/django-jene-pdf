from __future__ import unicode_literals 
from django.test import TestCase, Client
from jeneprocessor.jenepdf import JenePDF

class JeneTestCase(TestCase):
    def setUp(self):
        self._mclient = Client()
    

    def test_view_result(self):
        self._jenepdf = JenePDF('test_template.html', 'result.pdf')
        get_response = self._mclient.get('/renderjene')
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(get_response.__dict__['_headers']['content-disposition'][1],'attachment; filename=result.pdf')
        self.assertEqual(get_response.__dict__['_headers']['content-type'][1],'application/pdf')