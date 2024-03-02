from rest_framework import permissions


class IsAdminUserOrAuthorOrReadOnly(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user and request.user.is_staff:
            return True

        return obj.author == request.user
