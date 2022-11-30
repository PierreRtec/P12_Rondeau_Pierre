from rest_framework import permissions

"""CUSTOM PERMISSIONS"""


class IsAdmin(permissions.BasePermission):
    """
    Check if user is admin (manager)
    """
    def has_permission(self, request, view):
        user = request.user
        if user.is_superuser:
            return True

