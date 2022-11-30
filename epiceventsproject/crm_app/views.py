from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser, Contract, Customer, Event
from .permissions import IsSalesTeamGroup, IsManagementTeamGroup, IsSupportTeamGroup
from .serializers import (
    ContractSerializer,
    CustomerSerializer,
    EventSerializer,
    CustomUserSerializer,
)


# todo: est-ce que je peux mettre des décorateurs (ex: login_required) en plus ???


class CustomUserViewSet(viewsets.ModelViewSet):

    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsManagementTeamGroup]

    def get_queryset(self):
        return CustomUser.objects.all()


class CustomerViewSet(viewsets.ModelViewSet):
    """
    Customers view of Customer model.
    """

    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, IsSupportTeamGroup, IsSalesTeamGroup]

    def get_queryset(self):
        return Customer.objects.all()


class ContractViewSet(viewsets.ModelViewSet):
    """
    Contracts view of Contract model.
    """

    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, IsSupportTeamGroup, IsSalesTeamGroup]

    def get_queryset(self):
        return Contract.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    """
    Events view of Event model.
    """

    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsSupportTeamGroup, IsSalesTeamGroup]

    def get_queryset(self):
        return Event.objects.all()
