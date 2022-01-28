from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from ..forms import UserRegisterForm
from django.urls import reverse_lazy

# View for registration form
class UserRegistrationView(CreateView):
    
    form_class = UserRegisterForm
    success_url = '/login'
    template_name = 'register.html'
    
    def form_valid(self, form):
        self.request.session['username'] = form.cleaned_data['username']
        return super().form_valid(form)
    

# View for user login
class UserLoginView(LoginView):
    
    success_url=reverse_lazy("url-list")  # Redirect to the urls list on success
    
    def form_valid(self, form):
        self.request.session['username'] = form.cleaned_data['username']
        return super().form_valid(form)