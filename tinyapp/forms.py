from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm,TextInput
from .models import User,Url

#User registration form definition
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
    
#Create new short URL form definition
class UrlModelForm(ModelForm):
    class Meta:
        model = Url
        fields = ['long_url']
        widgets = {
            'long_url': TextInput(attrs={'placeholder': 'http://'})
        }