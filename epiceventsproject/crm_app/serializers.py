from rest_framework import serializers

from .models import CustomUser, Contract, Customer, Event


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "first_name", "last_name", "role")


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ("id", "sale_contact", "created_time", "updated_time")

    def _user(self):
        request = self.context.get("request", None)
        if request:
            return request.user

    def create(self, validated_data):
        customers = Customer.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            prospect=False,
            phone_number=validated_data["phone_number"],
            mobile_number=validated_data["mobile_number"],
            company_name=validated_data["company_name"],
            sales_contact=self._user(),
        )
        customers.save()
        return customers


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
        read_only_fields = ("id", "sale_contact", "created_time", "updated_time")

    def _user(self):
        request = self.context.get("request", None)
        if request:
            return request.user

    def create(self, validated_data):
        contracts = Contract.objects.create(
            status=True,
            amount=validated_data["amount"],
            sales_contact=self._user(),
            client=validated_data["client"],
            payment_due=validated_data["payment_due"],
        )
        contracts.save()  # on save le contrat
        contracts.client.prospect = False  # on set son att prospect à False
        contracts.client.save()  # on save le client du contrat
        return contracts


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ("id", "support_contact", "created_time", "updated_time")

    def _user(self):
        request = self.context.get("request", None)
        if request:
            return request.user

    def create(self, validated_data):
        events = Contract.objects.create(
            event_status=True,
            support_contact=self._user(),
            client=validated_data["client"],
            notes=validated_data["notes"],
            attendees=validated_data["attendees"],
            event_date=validated_data["event_date"],
        )
        events.save()
        return events
