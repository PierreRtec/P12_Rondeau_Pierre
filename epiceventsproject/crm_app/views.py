from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer, User


class RegisterViewSet(viewsets.ModelViewSet):
    """
    Create user account when first connexion, registration view.
    """
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return User.objects.all()

