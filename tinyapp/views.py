from typing import Generic
from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import Url, User
from .forms import UserRegisterForm

# Create your views here.
class UserRegistrationView(CreateView):
    form_class = UserRegisterForm
    success_url = '/register'
    template_name = 'register.html'
    
class UrlListView (ListView):    
    model = Url
    context_object_name = 'urls'   
    queryset = [{'short_url': 'b2xVn2', 
                 'long_url': 'https://www.google.com'}] 
    template_name = 'urls_index.html'

