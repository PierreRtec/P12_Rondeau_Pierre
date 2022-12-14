# Generated by Django 4.1.3 on 2022-12-14 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm_app", "0004_contract_event"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="sales_contact",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="event_sales_contact",
                to="crm_app.contract",
            ),
        ),
    ]
