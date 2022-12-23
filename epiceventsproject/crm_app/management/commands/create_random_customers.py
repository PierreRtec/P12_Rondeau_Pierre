import random

import faker.providers.bank
from django.core.management.base import BaseCommand
from faker import Faker

from crm_app.models import Customer


class Provider(faker.providers.BaseProvider):
    @staticmethod
    def create_customers(fake):
        """
        Creates N customers.
        Changes range to get the number of customers you want.
        """
        for _ in range(0):
            Customer.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.ascii_safe_email(),
                phone_number=fake.phone_number(),
                mobile_number=fake.phone_number(),
                company_name=fake.company(),
                prospect=random.randint(0, 1),
            )


class Command(BaseCommand):

    help = "Creation of random customers."

    def handle(self, *args, **options):

        fake = Faker(["fr-FR"])
        fake.add_provider(Provider)

        fake.create_customers(fake)
        print("created N customers successfully !")
