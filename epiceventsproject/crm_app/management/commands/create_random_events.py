import random

import faker.providers.bank
from django.core.management.base import BaseCommand
from faker import Faker
from crm_app.models import Event


class Provider(faker.providers.BaseProvider):

    @staticmethod
    def create_events(fake):
        """
        Creates N customers.
        Changes range to get the number of events you want.
        """
        for _ in range(1):
            Event.objects.create(
                        event_date=fake.future_date(),
                        attendees=fake.random_digit(),
                        notes=fake.paragraph(nb_sentences=2),
                        event_status=random.randint(0, 1),
            )


class Command(BaseCommand):

    help = "Creation of random events."

    def handle(self, *args, **options):

        fake = Faker(["fr-FR"])
        fake.add_provider(Provider)

        fake.create_events(fake)
        print("created N events successfully !")

