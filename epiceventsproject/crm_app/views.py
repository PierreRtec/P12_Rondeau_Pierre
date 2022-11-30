from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Contract, Customer, Event
from .serializers import (
    ContractSerializer,
    CustomerSerializer,
    EventSerializer,
    RegisterSerializer,
    User,
)


class RegisterViewSet(viewsets.ModelViewSet):
    """
    Create user account when first connexion, registration view.
    """

    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return User.objects.all()


class CustomerViewSet(viewsets.ModelViewSet):
    """
    Customers view of Customer models.
    """

    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Customer.objects.all()


class ContractViewSet(viewsets.ModelViewSet):
    """
    Contracts view of Contract models.
    """

    serializer_class = ContractSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Contract.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    """
    Contracts view of Contract models.
    """

    serializer_class = EventSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Event.objects.all()
