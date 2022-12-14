from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .management_user import UserManager


class CustomUser(AbstractUser):
    """
    super_user custom creation with UserManager
    """

    MANAGEMENT_TEAM = 1
    SUPPORT_TEAM = 2
    SALES_TEAM = 3

    ROLE_CHOICES = (
        (MANAGEMENT_TEAM, "management_team"),
        (SUPPORT_TEAM, "support_team"),
        (SALES_TEAM, "sales_team"),
    )

    role = models.PositiveSmallIntegerField(
        _("role"), choices=ROLE_CHOICES, blank=True, null=True
    )

    object = UserManager()

    class Meta:
        verbose_name = _("custom_user")
        verbose_name_plural = _("custom_users")
        ordering = ["role"]


class Customer(models.Model):
    objects = None

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    prospect = models.BooleanField(default=True)
    sales_contact = models.ForeignKey(
        to=CustomUser,
        related_name="sc_customer",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        prospect = self.prospect

        if prospect is False:
            prospect_or_customer = "customer"
        else:
            prospect_or_customer = "prospect"

        return f"{self.first_name} {self.last_name}, {prospect_or_customer}"


class Contract(models.Model):
    objects = None

    amount = models.FloatField()
    status = models.BooleanField(default=False, verbose_name="Signed")
    customer = models.ForeignKey(
        to=Customer,
        related_name="sc_customer_contract",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    sales_contact = models.ForeignKey(
        to=CustomUser,
        related_name="sc_contract",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    event = models.ForeignKey(
        to="Event",
        related_name="event_contract",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    payment_due = models.DateTimeField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        contract_status = self.status

        if contract_status is False:
            contract_status = "is not signed"
        else:
            contract_status = "is signed"

        return f"Contract n°{self.id}, customer : {self.customer}, status : {contract_status}"


class Event(models.Model):
    objects = None

    event_status = models.BooleanField(default=False, verbose_name="check if finished")
    customer = models.ForeignKey(
        to=Customer,
        related_name="sc_customer_event",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    contract = models.ForeignKey(
        to=Contract,
        related_name="event_contract",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    support_contact = models.ForeignKey(
        to=CustomUser,
        related_name="sc_event",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    notes = models.TextField(max_length=1024)
    attendees = models.IntegerField()
    event_date = models.DateTimeField(verbose_name="Example: 31/12/2022 10:02:44")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer}"
