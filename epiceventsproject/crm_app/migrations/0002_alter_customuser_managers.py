# Generated by Django 4.1.3 on 2022-12-12 13:40

import django.contrib.auth.models
import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("crm_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[
                ("object", django.db.models.manager.Manager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]