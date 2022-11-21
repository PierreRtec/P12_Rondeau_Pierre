# Generated by Django 4.1.3 on 2022-11-21 08:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=25, verbose_name="Joe")),
                ("last_name", models.CharField(max_length=25, verbose_name="Smith")),
                (
                    "email",
                    models.CharField(max_length=100, verbose_name="random@startup.io"),
                ),
                (
                    "phone_number",
                    models.CharField(max_length=20, verbose_name="639168088812"),
                ),
                (
                    "mobile_number",
                    models.CharField(max_length=20, verbose_name="639178089812"),
                ),
                (
                    "company_name",
                    models.CharField(max_length=250, verbose_name="Cool Startup Inc"),
                ),
                ("prospect", models.BooleanField(default=True)),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                ("updated_time", models.DateTimeField(auto_now=True)),
                (
                    "sales_contact",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="assignee_admin",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
