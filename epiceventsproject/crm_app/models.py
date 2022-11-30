from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


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
        to=AUTH_USER_MODEL,
        related_name="sc_customer",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class Contract(models.Model):

    objects = None

    amount = models.FloatField()
    status = models.BooleanField(default=True)
    client = models.ForeignKey(
        to=Customer,
        related_name="sc_customer_contract",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    sales_contact = models.ForeignKey(
        to=AUTH_USER_MODEL,
        related_name="sc_contract",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    payment_due = models.DateTimeField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class Event(models.Model):

    objects = None

    event_status = models.BooleanField(default=True)
    client = models.ForeignKey(
        to=Customer,
        related_name="sc_customer_event",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    support_contact = models.ForeignKey(
        to=AUTH_USER_MODEL,
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
