from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Contract, Customer, Event


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


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


class ProspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ("id", "sale_contact", "created_time", "updated_time")

    def _user(self):
        request = self.context.get("request", None)
        if request:
            return request.user

    def create(self, validated_data):
        prospects = Customer.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            prospect=True,
            phone_number=validated_data["phone_number"],
            mobile_number=validated_data["mobile_number"],
            company_name=validated_data["company_name"],
            sales_contact=self._user(),
        )
        prospects.save()
        return prospects


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
        contracts.save()
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
