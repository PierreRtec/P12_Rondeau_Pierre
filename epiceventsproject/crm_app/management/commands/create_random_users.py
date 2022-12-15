from random import randint

import faker.providers.bank
from django.core.management.base import BaseCommand
from faker import Faker

from crm_app.models import CustomUser


class Provider(faker.providers.BaseProvider):

    @staticmethod
    def create_custom_users(fake):
        """
        Creates 10 customs users to start using EpicEvents.
        """
        for _ in range(10):
            CustomUser.objects.create_user(
                        first_name=fake.first_name(),
                        last_name=fake.last_name(),
                        username=f"{fake.user_name()}{randint(1, 99)}",
                        password=fake.password(length=8),
                        email=fake.ascii_safe_email(),
                        role=randint(1, 3),
            )


class Command(BaseCommand):

    help = "Creation of random users."

    def handle(self, *args, **options):

        fake = Faker()
        fake.add_provider(Provider)

        fake.create_custom_users(fake)
        print("created 10 custom users successfully !")

