from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Contract, Customer, CustomUser, Event
from .permissions import GroupsPerms, IsAdmin, IsSalesTeam, IsSupportTeam
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
    permission_classes = [IsAuthenticated, IsAdmin, GroupsPerms]

    def get_queryset(self):
        return Group.objects.all()


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for /users/ API endpoint
    """
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_queryset(self):
        return CustomUser.objects.all()


class CustomerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for /customers/ API endpoint
    """
    serializer_class = CustomerSerializer
    permission_classes = [IsAdmin, IsAuthenticated, IsSalesTeam]

    def get_queryset(self):
        queryset_customer = Customer.objects.filter(sales_contact=self.request.user)
        return queryset_customer


class ContractViewSet(viewsets.ModelViewSet):
    """
    ViewSet for /contracts/ API endpoint
    """
    serializer_class = ContractSerializer
    permission_classes = [IsAdmin, IsAuthenticated, IsSalesTeam]

    def get_queryset(self):
        return Contract.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    """
    ViewSet for /events/ API endpoint
    """
    serializer_class = EventSerializer
    permission_classes = [IsAdmin, IsAuthenticated, IsSalesTeam]

    def get_queryset(self):
        return Event.objects.all()
