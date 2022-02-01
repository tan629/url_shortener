from django.shortcuts import render
from django.views.generic import CreateView,ListView,View, DeleteView, UpdateView
from ..models import Url, User, Visitor
from ..forms import UrlModelForm
import string,random
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.db.models import Count

def get_visitor_id():
    
    unique_str = ''.join(random.choice(string.digits + string.ascii_uppercase) for i in range(6)) 
    
    return 'Visitor_' + unique_str

# This function sets the cookie to track visitor data          
def set_cookie_visitor_data(short_url, response, request):

    user_logged_in = request.session.get('username')
        
    cookie_id = 'Visitor_' + short_url # Set cookie for anonymous user
    
    if user_logged_in:
        cookie_id += str(user_logged_in) # Set cookie unqiue to the logged in user

    if user_logged_in == None:
        visitor = Visitor(visitor_id=get_visitor_id(), short_url=short_url)
    else:
        if cookie_id in request.COOKIES.keys():
            visitor = Visitor(visitor_id=request.COOKIES[cookie_id], short_url=short_url)
            
        else: # Generate a visitor ID for the logged in user only if the user is viewing the short url for first time   
            visitor = Visitor(visitor_id=get_visitor_id(), short_url=short_url)
            response.set_cookie(cookie_id,visitor.visitor_id,max_age=1000000)
    
    if visitor:
        visitor.save()
            

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
        form.instance.slug_field = slugify(form.instance.long_url + form.instance.short_url)

        return super().form_valid(form) #If form fields are valid, it redirects to success_url defined in this class
    
    # Get coookie info from context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username') # Set cookie in the context object
        
        return context
    
    
# View that redirects a short URL to its corresponding long URL
class UrlRedirectView(View):
    
    def get(self, request, short_url):  
        
        self.short_url = short_url
             
        url_obj = Url.objects.filter(short_url=short_url) #Get URL object from database table of URL based on given short URL  
        
        response = HttpResponseRedirect(url_obj[0].long_url)
        
        #Track visitors 
       
        set_cookie_visitor_data(short_url,response,request)
            
        return response

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
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username') # Set cookie in the context object
                 
        # Query visitor data of the given url       
        query_set = Visitor.objects.filter(short_url=str(context['url']))
        
        # Set the visitors data table for display in the url detail page
        context['visitors'] = query_set
        
        #Set the total visits variable to be displayed on the URL detail page
        context['total_visits'] = query_set.count()
        
        # Set the number of unique visits to the given short URL for display on the URL detail page
        
        context['unique_visits'] = query_set.values('visitor_id').annotate(dcount=Count('visitor_id')).order_by().count()
  
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