from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Contract, Customer, CustomUser, Event
from .permissions import IsAdmin, IsSalesTeam, IsSupportTeam
from .serializers import (
    ContractSerializer,
    CustomerSerializer,
    CustomUserSerializer,
    EventSerializer,
)


class CustomUserViewSet(viewsets.ModelViewSet):

    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_queryset(self):
        return CustomUser.objects.all()


class CustomerViewSet(viewsets.ModelViewSet):
    """
    Customers view of Customer model.
    """

    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, IsSupportTeam, IsSalesTeam]

    def get_queryset(self):
        return Customer.objects.all()


class ContractViewSet(viewsets.ModelViewSet):
    """
    Contracts view of Contract model.
    """

    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, IsSupportTeam, IsSalesTeam]

    def get_queryset(self):
        return Contract.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    """
    Events view of Event model.
    """

    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsSupportTeam, IsSalesTeam]

    def get_queryset(self):
        return Event.objects.all()
