from django.views.generic import ListView
from ..models import User

# View for user login
class SeeAdminsView(ListView):
    
    template_name = 'admin.html'
    model = User   
    context_object_name = 'users'
    
    # Get coookie info from context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username')

        return context
    
    def get_queryset(self):
        
        current_user_id = self.request.user.id
        print("PERM = ",self.request.user.has_perm('tinyapp.view_user'))
        if current_user_id == None or self.request.user.has_perm('tinyapp.view_user') == False:
            return None
        
        return User.objects.filter() 