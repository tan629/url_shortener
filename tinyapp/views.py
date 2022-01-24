from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from .forms import UserRegisterForm

# Create your views here.
class UserRegistrationView(CreateView):
    form_class = UserRegisterForm
    success_url = '/register'
    template_name = 'register.html'

