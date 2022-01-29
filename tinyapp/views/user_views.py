from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from ..forms import UserRegisterForm

# View for registration form
class UserRegistrationView(CreateView):
    
    form_class = UserRegisterForm
    success_url = '/login'
    template_name = 'register.html'
    
    def form_valid(self, form):
        
        return super().form_valid(form)
    

# View for user login
class UserLoginView(LoginView):
    
    def form_valid(self, form):
        
        # Set the session cookie on successful login
        self.request.session['username'] = form.cleaned_data['username']
        
        return super().form_valid(form)