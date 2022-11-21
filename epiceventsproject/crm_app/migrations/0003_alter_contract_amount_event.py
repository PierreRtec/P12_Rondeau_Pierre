# Generated by Django 4.1.3 on 2022-11-21 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("crm_app", "0002_alter_customer_company_name_alter_customer_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="amount",
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name="Event",
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
                ("event_status", models.BooleanField(default=True)),
                ("notes", models.TextField(max_length=1024)),
                ("attendees", models.IntegerField()),
                (
                    "event_date",
                    models.DateTimeField(verbose_name="Example: 31/12/2022 10:02:44"),
                ),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                ("updated_time", models.DateTimeField(auto_now=True)),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sc_customer_event",
                        to="crm_app.customer",
                    ),
                ),
                (
                    "support_contact",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="sc_event",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
