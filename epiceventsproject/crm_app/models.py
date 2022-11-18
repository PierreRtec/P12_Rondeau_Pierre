from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Customer(models.Model):

    objects = None
    first_name = models.CharField(max_length=25, verbose_name="Joe")
    last_name = models.CharField(max_length=25, verbose_name="Smith")
    email = models.CharField(max_length=100, verbose_name="random@startup.io")
    phone_number = models.CharField(max_length=20, verbose_name="639168088812")
    mobile_number = models.CharField(max_length=20, verbose_name="639178089812")
    company_name = models.CharField(max_length=250, verbose_name="Cool Startup Inc")
    prospect = models.BooleanField(
        default=True
    )  # permet de savoir si un client est un prospect (=potentiel client) ou non
    sales_contact = models.ForeignKey(
        to=AUTH_USER_MODEL,
        related_name="assignee_admin",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
