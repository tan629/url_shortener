from django.views.generic import ListView
from ..models import User
from django.contrib.auth.mixins import PermissionRequiredMixin

# View for user login
class SeeAdminsView(PermissionRequiredMixin,ListView):
    
    permission_required = 'tinyapp.view_user'
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
        
        if current_user_id == None or self.request.user.has_perm('tinyapp.view_user') == False:
            return None
        
        return User.objects.all() 