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