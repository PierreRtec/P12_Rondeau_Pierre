from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Customer
from .serializers import RegisterSerializer, User, CustomerSerializer


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
        return Customer.objects.filter(prospect=False)
