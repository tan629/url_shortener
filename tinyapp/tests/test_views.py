import datetime
from django.test import TestCase,Client
from tinyapp.models import User, Url

class ViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="Katherine",
            last_name="Johnson",
            username="KJ",
            email="mathematics@nasa.com",
            is_staff=False,
            is_active=True,
            is_superuser=False
        )
        
        self.user.set_password("!P4s5w0*d")
        self.user.save()
        
        self.url_1 = Url.objects.create(
            short_url='bx2Vu2',
            long_url='https://www.google.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        
        self.url_2 = Url.objects.create(
            short_url='bx2Vr3',
            long_url='https://www.facebook.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        
        self.url_3 = Url.objects.create(
            short_url='bx2Vx4',
            long_url='https://www.amazon.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        
        self.url_4 = Url.objects.create(
            short_url='bx2Vn5',
            long_url='https://www.youtube.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        
        self.url_5 = Url.objects.create(
            short_url='bx2Vm6',
            long_url='https://www.bbc.com',
            user=self.user,
            date_created=datetime.datetime.now()
        )
        
        self.url_1.save()
        
    # Test GET requests       
    def test_get_requests(self):
        c = Client()
        response = c.get('/urls/')
        
        self.assertEqual(response.status_code, 302)
        
    def test_url_list_view_logged_in(self):
        
        c = Client()
        
        login_response = c.post('/login/',{'username':'KJ', 'password':'!P4s5w0*d'})    
        self.assertEqual(login_response.status_code, 302)
          
        #Test URLs list for logged in user
        response = c.get('/urls/') 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['urls']), 5)       
        self.assertTemplateUsed(response, 'urls_index.html')
        
        #Test new URL view for logged in user
        response = c.get('/urls/new/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'urls_new.html')
        
        # Expected result is 403 forbidden error since the user is not authorized to see users list
        response = c.get('/userlist/')
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, '403.html')
        
        
    def test_url_list_view_logged_out(self):
        
        c = Client()
        
        response = c.get('/urls/') 
        self.assertEqual(response.status_code,302) #Should redirect to login page for anonymous user
        
        response = c.get('/urls/new/')
        self.assertEqual(response.status_code, 302)
            