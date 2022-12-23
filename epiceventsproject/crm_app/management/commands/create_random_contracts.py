import random

import faker.providers.bank
from django.core.management.base import BaseCommand
from faker import Faker

from crm_app.models import Contract


class Provider(faker.providers.BaseProvider):
    @staticmethod
    def create_contracts(fake):
        """
        Creates N contract.
        Changes range to get the number of contracts you want.
        """
        for _ in range(1):
            Contract.objects.create(
                amount=round(random.uniform(100, 10000), 3),
                status=random.randint(0, 1),
                payment_due=fake.date(),
            )


class Command(BaseCommand):

    help = "Creation of random contracts."

    def handle(self, *args, **options):

        fake = Faker(["fr-FR"])
        fake.add_provider(Provider)

        fake.create_contracts(fake)
        print("created N contracts successfully !")
