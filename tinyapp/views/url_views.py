from django.shortcuts import render
from django.views.generic import CreateView,ListView,View, DeleteView, UpdateView
from ..models import Url, User
from ..forms import UrlModelForm
import string,random
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# View for displaying URLs saved in the database
class UrlListView (LoginRequiredMixin,ListView):  
    
    login_url = '/login'
    
    model = Url   
    context_object_name = 'urls'

    template_name = 'urls_index.html'
    
    # Get coookie info from context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username')

        return context
    
    def get_queryset(self):
        
        current_user_id = self.request.user.id
        
        if current_user_id == None:
            return None
        
        return Url.objects.filter(user_id=current_user_id) 

# View for creating a new short URL
class UrlCreateView(LoginRequiredMixin,CreateView):
    
    login_url = '/login/'
    form_class = UrlModelForm
    success_url = '/urls'
    template_name = 'urls_new.html'
    
    #This method generates a short URL
    def get_short_url(self):
        letters = string.ascii_lowercase + string.digits + string.ascii_uppercase
        return ''.join(random.choice(letters) for i in range(6))

    #Validate the create URL form
    def form_valid(self, form):
        
        current_user_id = self.request.user.id
        user = User.objects.filter(pk = current_user_id).first()
        form.instance.user = user
        form.instance.short_url = self.get_short_url()

        return super().form_valid(form) #If form fields are valid, it redirects to success_url defined in this class
    
    # Get coookie info from context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username') # Set cookie in the context object
        
        return context
    
    
# View that redirects a short URL to its corresponding long URL
class UrlRedirectView(View):
    
    def get(self, request, short_url):       
        url_obj = Url.objects.filter(short_url=short_url) #Get URL object from database table of URL based on given short URL   
        return HttpResponseRedirect(url_obj[0].long_url)
    

# View that deletes the specified URL from the URL table
class UrlDeleteView(DeleteView):
       
    model=Url
    success_url=reverse_lazy("url-list") #Redirect to the urls list
    
# View to update URL
class UrlUpdateView(UpdateView):

    model = Url
    form_class = UrlModelForm
    template_name = 'url_detail.html' # template for updating URL
    success_url=reverse_lazy("url-list")  # Redirect to the urls list on success
    
    # Get coookie info from context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username') # Set cookie in the context object
        
        return context

    def get(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        
        logged_in_user = self.request.session.get('username')
        
        logged_in_user_id = None
        
        if logged_in_user:
            logged_in_user_id = User.objects.filter(username=logged_in_user)[0].id
        
        #Check if the user id of the URL object is same as the logged in user id
        #If not, then deny access to the URL
        if(self.object.user_id != logged_in_user_id):
            return HttpResponseForbidden()
        
        return super().get(request, *args, **kwargs)