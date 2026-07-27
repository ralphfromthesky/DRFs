from rest_framework.permissions import BasePermission

class IsAdminRole(BasePermission):
    # message = 'jakol ka muna'
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        try:
            return request.user.userprofile.role == 'admin'
        except:
            return False
        

class RoleBasedPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        try:
            role = request.user.userprofile.role
        except:
            return False
        
        if role == 'viewer':
            return request.method in ['GET', 'POST']
        
        if role == 'editor':
            return request.method in ['GET', 'PUT', 'PATCH']
        
        if role == 'admin':
            return request.method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
        
        return False