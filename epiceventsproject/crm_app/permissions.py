from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions

from crm_app.models import CustomUser
from rest_framework.permissions import IsAdminUser

"""CUSTOM PERMISSIONS"""


# groups permissions
class GroupsPerms(permissions.BasePermission):
    # django basics perms (het, head, options)
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    # django basics obj perms (het, head, options)
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


# permissions for managers
class IsAdmin(permissions.BasePermission):
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
