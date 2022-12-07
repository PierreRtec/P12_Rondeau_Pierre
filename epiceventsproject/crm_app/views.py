from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Contract, Customer, CustomUser, Event
from .permissions import GroupsPerms, SalesTeam, SupportTeam
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
    permission_classes = [IsAuthenticated, GroupsPerms, SalesTeam]

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


class CustomerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for /customers/ API endpoint
    """

    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, SupportTeam | SalesTeam]

    def get_queryset(self):
        # sales team
        if self.request.user.role == 3:
            return Customer.objects.filter(sales_contact=self.request.user)
        # support team
        elif self.request.user.role == 2:
            return Customer.objects.filter(sales_contact=self.request.user)
        # admin
        elif self.request.user.role == 1:
            return Customer.objects.all()


class ContractViewSet(viewsets.ModelViewSet):
    """
    ViewSet for /contracts/ API endpoint
    """

    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, SupportTeam | SalesTeam]

    def get_queryset(self):
        return Contract.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    """
    ViewSet for /events/ API endpoint
    """

    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, SupportTeam | SalesTeam]

    def get_queryset(self):
        return Event.objects.all()
