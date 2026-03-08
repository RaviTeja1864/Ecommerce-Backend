from django.core.management.base import BaseCommand
from faker import Faker
import random
from store.models import Product, Collection
from django.utils import timezone


class Command(BaseCommand):
    help = "Seed products"

    def handle(self, *args, **kwargs):

        fake = Faker()

        collections = list(Collection.objects.all())

        # If no collections exist, create some
        if not collections:
            for _ in range(10):
                collections.append(
                    Collection.objects.create(
                        title=fake.word().capitalize()
                    )
                )

        for _ in range(500):
            Product.objects.create(
                title=fake.word().capitalize(),
                price=random.uniform(10, 500),
                description=fake.text(),
                inventory=random.randint(1, 100),
                last_update=timezone.now(),
                collection=random.choice(collections)
            )

        self.stdout.write(self.style.SUCCESS("Products seeded successfully"))