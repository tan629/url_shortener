import datetime
from django.test import TestCase
from tinyapp.models import User, Url

class UrlTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="Katherine",
            last_name="Johnson",
            username="KJ",
            email="mathematics@nasa.com",
            password="!P4s5w0*d",
            is_staff=False,
            is_active=True,
            is_superuser=False
        )
        self.url = Url.objects.create(
            short_url='bx2Vn2',
            long_url='https://www.google.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )

    def test_long_url(self):
        url= Url.objects.get(pk=self.url.pk)
        self.assertEqual('https://www.google.com', url.long_url)

    def test_model_user(self):
        user = User.objects.get(pk=self.user.pk)
        self.assertEqual('Katherine', user.first_name)
        
    def test_url_str(self):
        url = Url.objects.get(pk=self.url.pk)
        self.assertEqual(str(url), 'bx2Vn2')

    def test_url_absolute(self):
        url = Url.objects.get(pk=self.url.pk)
        self.assertEqual(f'/urls/{self.url.pk}/', url.get_absolute_url())
        
    def test_model_user_full_name(self):
        user = User.objects.get(pk=self.user.pk)
        self.assertEqual('Katherine Johnson', str(user))