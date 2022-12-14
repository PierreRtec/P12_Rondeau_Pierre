from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import SAFE_METHODS

from .models import Contract, Event

"""CUSTOM PERMISSIONS"""


class CustomersPerms(permissions.BasePermission):
    """
    PERMISSIONS CUSTOMERS

    MANAGEMENT TEAM
    - READE ONLY, safe methods ?

    SALES TEAM
    - POST CUSTOMERS
    - GET and PUT CUSTOMERS

    SUPPORT TEAM
    - GET OWN CUSTOMERS
    """

    def has_object_permission(self, request, view, obj):
        # if user role manager, grant all or read only ??
        if view.action and request.user.role == 1:
            return True

        # if get post put and sales
        if view.action in ("create", "retrieve", "update") and request.user.role == 3:
            return request.user == obj.sales_contact

        # if get and support
        if view.action == "retrieve" and request.user.role == 2:
            return Event.objects.filter(support_contact=request.user)  # todo: check si toujours utile

        else:
            raise PermissionDenied("You do not have permission.")


class ContractPerms(permissions.BasePermission):
    """
    PERMISSIONS CONTRACT
    MANAGEMENT TEAM
    - READE ONLY, safe methods ?

    SALES TEAM
    - POST CONTRACTS
    - GET and PUT OWN CUSTOMERS if not finished

    SUPPORT TEAM
    - GET CONTRACTS OWN CUSTOMERS
    """

    def has_object_permission(self, request, view, obj):
        # if user role manager
        if view.action and request.user.role == 1:
            return True

        # if get post put and sales
        if view.action in ("create", "retrieve", "update") and request.user.role == 3:
            return request.user == obj.contract.sales_contact

        else:
            raise PermissionDenied("You do not have permission.")


class EventsPerms(permissions.BasePermission):
    """
    PERMISSIONS EVENTS /

    MANAGEMENT TEAM
    - READE ONLY, safe methods ?

    SALES TEAM
    - POST NEW EVENTS
    - GET and PUT EVENTS OF THEIR CUSTOMERS (if contract isn't finished)

    SUPPORT TEAM
    - VIEW EVENTS OF THEIR CUSTOMERS
    - PUT EVENTS OF THEIR CUSTOMERS (if contract isn't finished)
    """

    def has_object_permission(self, request, view, obj):

        # if user role manager
        if view.action and request.user.role == 1:
            return True
        # if get post put and sales
        if view.action in ("create", "retrieve", "update") and request.user.role == 3:
            return request.user == obj.event.sales_contact
        if view.action == "retrieve" and request.user.role == 2:
            return Event.objects.filter(support_contact=request.user)
        else:
            raise PermissionDenied("You do not have permission.")
