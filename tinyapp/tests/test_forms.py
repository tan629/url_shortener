from django.test import TestCase
from tinyapp.models import User
from tinyapp.forms import UrlModelForm

class TestUrlModelForm(TestCase):
    
    def test_empty_form(self):
        form = UrlModelForm()
        self.assertIn('long_url', form.fields)
        self.assertIn('placeholder="https://"', form.as_p())
        self.assertIn('class="form-control bg-info"', form.as_p())
        
        self.fail(form.as_p())
        