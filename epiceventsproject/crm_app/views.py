from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Contract, Customer, CustomUser, Event
from .permissions import RolesPermissions
from .serializers import (
    ContractSerializer,
    CustomerSerializer,
    CustomUserSerializer,
    EventSerializer,
    GroupSerializer,
)


class GroupViewSet(viewsets.ModelViewSet):
    """
    ViewSet for /groups/ API endpoint
    """

    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Group.objects.all()


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for /users/ API endpoint
    """

    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.all()


# todo check perms
class CustomerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for /customers/ API endpoint
    """

    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, RolesPermissions]

    def get_queryset(self):
        # sales team
        if self.request.user.role == 3:
            return Customer.objects.filter(sales_contact=self.request.user)
        # support team
        elif self.request.user.role == 2:
            return Customer.objects.filter(support_contact=self.request.user)
        # admin
        elif self.request.user.role == 1:
            return Customer.objects.all()


# todo perm sales support
class ContractViewSet(viewsets.ModelViewSet):
    """
    ViewSet for /contracts/ API endpoint
    """

    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, RolesPermissions]

    # on renvoie que les objets liés a celui qui request # todo
    def get_queryset(self):
        # sales team
        if self.request.user.role == 3:
            return Contract.objects.filter(sales_contact=self.request.user)
        # support team
        elif self.request.user.role == 2:
            return Contract.objects.filter(support_contact=self.request.user)
        # admin
        elif self.request.user.role == 1:
            return Contract.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    """
    ViewSet for /events/ API endpoint
    """

    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, RolesPermissions]

    # on renvoie que les objets liés a celui qui request # todo
    # si user support get un objet pas à lui, peut pas, si objet a lui il peut
    def get_queryset(self):
        # sales team
        if self.request.user.role == 3:
            return Event.objects.filter(sales_contact=self.request.user)
        # support team
        elif self.request.user.role == 2:
            return Event.objects.filter(support_contact=self.request.user)
        # admin
        elif self.request.user.role == 1:
            return Event.objects.all()
