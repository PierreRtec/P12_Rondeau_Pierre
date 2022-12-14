from django.contrib.auth.models import Group
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from .models import Contract, Customer, CustomUser, Event
from .permissions import ContractPerms, CustomersPerms, EventsPerms
from .serializers import (
    ContractSerializer,
    CustomerSerializer,
    CustomUserSerializer,
    EventSerializer,
    GroupSerializer,
)


class GroupViewSet(viewsets.ModelViewSet):
    """
    ViewSet for "/groups/" API endpoint
    """

    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Group.objects.all()


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for "/users/" API endpoint
    """

    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.all()


class CustomerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for "/customers/" API endpoint
    """

    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, CustomersPerms]
    filter_backends = [DjangoFilterBackend]
    search_fields = ["^first_name", "^last_name", "^company_name"]
    ordering_fields = ["^first_name", "^last_name"]
    filterset_fields = ["prospect"]

    def get_queryset(self):
        # sales #marketing
        if self.request.user.role == 3:
            return Customer.objects.filter(sales_contact=self.request.user)

        # support_team
        elif self.request.user.role == 2:
            return [event.customer for event in self.request.user.sc_event.all()]

        # admin
        elif self.request.user.role == 1:
            return Customer.objects.all()


class ContractViewSet(viewsets.ModelViewSet):
    """
    ViewSet for "/contracts/" API endpoint
    """

    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, ContractPerms]
    filter_backends = [DjangoFilterBackend]
    search_fields = ["^customer__first_name", "^customer__last_name", "customer__^company_name"]
    ordering_fields = ["^customer__first_name", "^customer__last_name"]
    filterset_fields = ["created_time", "updated_time"]

    def get_queryset(self):
        # sales #marketing
        if self.request.user.role == 3:
            return Contract.objects.filter(sales_contact=self.request.user)

        # support
        elif self.request.user.role == 2:
            return [event.event_contract for event in self.request.user.sc_event.all()]

        # admin
        elif self.request.user.role == 1:
            return Contract.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    """
    ViewSet for "/events/" API endpoint
    """

    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, EventsPerms]
    filter_backends = [DjangoFilterBackend]
    search_fields = []
    ordering_fields = []
    filterset_fields = []

    def get_queryset(self):
        # sales #marketing
        if self.request.user.role == 3:
            return Event.objects.filter(contract__sales_contact=self.request.user)

        # support
        elif self.request.user.role == 2:
            return Event.objects.filter(support_contact=self.request.user)

        # admin
        elif self.request.user.role == 1:
            return Event.objects.all()
