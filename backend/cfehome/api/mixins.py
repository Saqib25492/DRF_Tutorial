from .permissions import IsStaffEditor
from rest_framework import permissions    
from django.db.models import Q                         

class StaffEditorMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditor]
    
    
class UserQuerySetMixin():
    user_field = 'user'
    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        user = self.request.user
        lookup_data[self.user_field] = user.id
        qs = super().get_queryset(*args, **kwargs) 
        print(user, user.id)
        if user.id is None:
            return qs.filter(public=True)
        return (qs.filter(**lookup_data) | qs.filter(public=True)).distinct()