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


# permissions for sales_team
class IsSalesTeam(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.groups.filter(name="sales_team").exists():
            return True
        # check if is_superuser (True par défaut dans management_user)
        elif user.is_superuser:
            return True
        # role user returned for sales team
        return request.user.role == 2


# permissions for support_team
class IsSupportTeam(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.groups.filter(name="support_team").exists():
            return True
