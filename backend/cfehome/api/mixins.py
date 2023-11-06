from .permissions import IsStaffEditor
from rest_framework import permissions                              

class StaffEditorMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditor]
    
    
class UserQuerySetMixin():
    user_field = 'user'
    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        user = self.request.user
        lookup_data[self.user_field] = user
        qs = super().get_queryset(*args, **kwargs) 
    
        return qs.filter(**lookup_data)  