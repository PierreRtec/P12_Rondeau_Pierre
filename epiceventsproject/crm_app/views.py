from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Customer
from .serializers import (
    CustomerSerializer,
    ProspectSerializer,
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


# todo : check si possible prospect OU client lors d'un POST, sinon laisser comme ça
class ProspectViewSet(viewsets.ModelViewSet):
    """
    Prospects view of Customer models.
    """

    serializer_class = ProspectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Customer.objects.all()
