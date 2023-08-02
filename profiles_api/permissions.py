from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_obj_permission(self,request,view,obj):
        """Checking to see if the user is trying to edit their own pf"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id