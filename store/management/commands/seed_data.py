from django.core.management.base import BaseCommand
from faker import Faker
import random
from store.models import Product, Collection


class Command(BaseCommand):
    help = "Seed the database with sample products and collections"

    def handle(self, *args, **kwargs):
        fake = Faker()

        collections = list(Collection.objects.all())

        if not collections:
            for _ in range(10):
                collections.append(
                    Collection.objects.create(title=fake.word().capitalize())
                )
            self.stdout.write(f"Created {len(collections)} collections")

        for _ in range(500):
            Product.objects.create(
                title=fake.catch_phrase(),
                price=round(random.uniform(10, 500), 2),
                description=fake.text(),
                inventory=random.randint(1, 100),
                collection=random.choice(collections)
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded 500 products"))
