import os
import django
import random
from decimal import Decimal
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Collection, Product
from customers.models import Customer
from orders.models import Order, OrderItem
from carts.models import Cart, CartItem
from faker import Faker

fake = Faker(['en_IN'])


def seed_db():
    print("--- Starting Database Seed ---")

    # 1. Create Collections
    categories = [
        'Electronics', 'Home Appliances', 'Mens Fashion', 'Womens Fashion',
        'Beauty & Care', 'Groceries', 'Books', 'Fitness', 'Toys', 'Furniture'
    ]
    col_objs = []
    for title in categories:
        col, _ = Collection.objects.get_or_create(title=title)
        col_objs.append(col)
    print(f"Created {len(col_objs)} Collections")

    # 2. Create 50 Products
    product_objs = []
    for _ in range(50):
        prod = Product.objects.create(
            title=fake.catch_phrase(),
            price=Decimal(random.uniform(99, 4999)).quantize(Decimal('0.00')),
            inventory=random.randint(5, 200),
            collection=random.choice(col_objs),
            description=fake.paragraph(nb_sentences=3),
        )
        product_objs.append(prod)
    print(f"Created {len(product_objs)} Products")

    # 3. Create 100 Customers
    customer_objs = []
    memberships = ['B', 'S', 'G']
    for _ in range(100):
        cust = Customer.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.unique.email(),
            membership=random.choice(memberships)
        )
        customer_objs.append(cust)
    print(f"Created {len(customer_objs)} Customers")

    # 4. Create 50 Orders with Items
    for _ in range(50):
        order = Order.objects.create(
            placed_at=fake.date_time_this_year(
                before_now=True,
                after_now=False,
                tzinfo=timezone.get_current_timezone()
            ),
            payment_status=random.choice(['P', 'C', 'F']),
            customer=random.choice(customer_objs)
        )
        # Use unique products per order to avoid constraint issues
        selected_products = random.sample(product_objs, k=random.randint(1, 4))
        for p in selected_products:
            OrderItem.objects.create(
                order=order,
                product=p,
                quantity=random.randint(1, 3),
                unit_price=p.price
            )
    print("Created 50 Orders with line items")

    # 5. Create a Cart with items (unique products only)
    cart = Cart.objects.create()
    selected_products = random.sample(product_objs, k=10)
    for p in selected_products:
        CartItem.objects.create(
            cart=cart,
            product=p,
            quantity=random.randint(1, 2)
        )
    print("Created 1 Cart with 10 Items")

    print("\n--- Database Seeding Complete ---")


if __name__ == "__main__":
    seed_db()
