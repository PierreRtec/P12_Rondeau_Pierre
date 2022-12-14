from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

from .models import Event

"""CUSTOM PERMISSIONS"""


class CustomersPerms(permissions.BasePermission):
    """
    PERMISSIONS CUSTOMERS

    MANAGEMENT TEAM
    - ALL

    SALES TEAM
    - POST CUSTOMERS
    - GET and PUT CUSTOMERS

    SUPPORT TEAM
    - GET OWN CUSTOMERS
    """

    def has_object_permission(self, request, view, obj):
        if view.action and request.user.role == 1:
            return True

        if view.action in ("create", "retrieve", "update") and request.user.role == 3:
            return request.user == obj.sales_contact

        if view.action == "retrieve" and request.user.role == 2:
            return Event.objects.filter(support_contact=request.user)

        else:
            raise PermissionDenied("You do not have permission.")


class ContractPerms(permissions.BasePermission):
    """
    PERMISSIONS CONTRACT
    MANAGEMENT TEAM
    - ALL

    SALES TEAM
    - POST CONTRACTS
    - GET and PUT OWN CUSTOMERS if not finished

    SUPPORT TEAM
    - GET CONTRACTS OWN CUSTOMERS
    """

    def has_object_permission(self, request, view, obj):
        if view.action and request.user.role == 1:
            return True

        if view.action in ("create", "retrieve", "update") and request.user.role == 3:
            return request.user == obj.sales_contact

        else:
            raise PermissionDenied("You do not have permission.")


class EventsPerms(permissions.BasePermission):
    """
    PERMISSIONS EVENTS /

    MANAGEMENT TEAM
    - ALL

    SALES TEAM
    - POST NEW EVENTS
    - GET and PUT EVENTS OF THEIR CUSTOMERS

    SUPPORT TEAM
    - VIEW EVENTS OF THEIR CUSTOMERS
    - PUT EVENTS OF THEIR CUSTOMERS
    """

    def has_object_permission(self, request, view, obj):
        if view.action and request.user.role == 1:
            return True

        if view.action in ("create", "retrieve", "update") and request.user.role == 3:
            return request.user == obj.sales_contact

        if view.action in ("retrieve", "update") and request.user.role == 2:
            return Event.objects.filter(support_contact=request.user)

        else:
            raise PermissionDenied("You do not have permission.")
