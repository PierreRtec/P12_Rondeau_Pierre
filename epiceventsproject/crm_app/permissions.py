from rest_framework import permissions

"""CUSTOM PERMISSIONS"""


# todo: permissions management_team
class IsManagementTeamGroup(permissions.BasePermission):
    """
    Check if
    http_methods :
    """

    def has_permission(self, request, view):

        return True


# todo: permissions sales_team
class IsSalesTeamGroup(permissions.BasePermission):
    """
    Check if
    http_methods :
    """

    def has_permission(self, request, view):

        return True


# todo: permissions support_team
class IsSupportTeamGroup(permissions.BasePermission):
    """
    Check if
    http_methods :
    """

    def has_permission(self, request, view):

        return True
