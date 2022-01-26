from typing import Generic
from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,View, DeleteView
from .models import Url, User
from .forms import UrlModelForm, UserRegisterForm
import string,random
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.

# View for registration form
class UserRegistrationView(CreateView):
    
    form_class = UserRegisterForm
    success_url = '/register'
    template_name = 'register.html'
    
# View for displaying URLs saved in the database
class UrlListView (ListView):  
      
    model = Url   
    context_object_name = 'urls'  
    queryset = model.objects.all()
    template_name = 'urls_index.html'

# View for creating a new short URL
class UrlCreateView(CreateView):
    
    form_class = UrlModelForm
    success_url = '/urls'
    template_name = 'urls_new.html'
    
    def post(self, request):
        form = self.form_class(request.POST) 
        return self.form_valid(form)
        
    def get_short_url(self):
        letters = string.ascii_lowercase + string.digits + string.ascii_uppercase
        return ''.join(random.choice(letters) for i in range(6))

    def form_valid(self, form):
        user_id = User.objects.filter(username="tamin").values_list('id',flat=True)
        
        form.instance.user_id = user_id
        form.instance.short_url = self.get_short_url()

        return super().form_valid(form) #If form fields are valid, it redirects to success_url defined in this class
    
# View for creating a new short URL
class UrlDetailView (DetailView):
        
    model = Url
    context_object_name = 'url'   
    template_name = 'url_detail.html'
    
    def get(self,request,pk):
        
        url = Url.objects.filter(id=pk).first()
        
        context={
            self.context_object_name :url
        }
        
        return render(request, self.template_name,context)

# View that redirects a short URL to its corresponding long URL

class UrlRedirectView(View):
    
    def get(self, request, short_url): 
               
        url_obj = Url.objects.filter(short_url=short_url) #Get URL object from database table of URL based on given short URL     
        return HttpResponseRedirect(url_obj[0].long_url)
    
# View that deletes the specified URL from the URL table
class UrlDeleteView(DeleteView):
       
    model=Url
    template_name='delete_view.html'
    success_url=reverse_lazy("url-list") #Redirect to the urls list
    

