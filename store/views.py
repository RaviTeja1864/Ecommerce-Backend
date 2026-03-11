from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Q, F
from .models import Product, Collection


# 1. List all products (using select_related)
def product_list(request):
    products = Product.objects.select_related('collection')

    return render(request, 'products.html', {'products': products})


# 2. Show products for each collection (prefetch_related)
def collections_products(request):
    collections = Collection.objects.prefetch_related('product_set')

    result = ""

    for c in collections:
        result += f"<h3>{c.title}</h3>"
        for p in c.product_set.all():
            result += f"{p.title}<br>"

    return HttpResponse(result)


# 3. Count products in each collection (annotate)
def collections_with_product_count(request):

    collections = Collection.objects.annotate(
        product_count=Count('product')
    )

    result = ""

    for c in collections:
        result += f"{c.title} - {c.product_count} products<br>"

    return HttpResponse(result)


# 4. Return specific fields (values)
def product_titles_prices(request):

    products = Product.objects.values('title', 'unit_price')[:10]

    result = ""

    for p in products:
        result += f"{p['title']} - {p['unit_price']}<br>"

    return HttpResponse(result)


# 5. Return tuple results (values_list)
def product_titles_prices_list(request):

    products = Product.objects.values_list('title', 'unit_price')[:10]

    result = ""

    for title, price in products:
        result += f"{title} - {price}<br>"

    return HttpResponse(result)


# 6. Complex filtering using Q objects
def cheap_or_high_inventory(request):

    products = Product.objects.filter(
        Q(unit_price__lt=20) | Q(inventory__gt=50)
    )[:20]

    result = ""

    for p in products:
        result += f"{p.title} - price:{p.unit_price} inventory:{p.inventory}<br>"

    return HttpResponse(result)


# 7. Update inventory using F expression
def increase_inventory(request):

    Product.objects.filter(id=1).update(
        inventory=F('inventory') + 5
    )

    return HttpResponse("Inventory updated")


# 8. Show product details
def product_detail(request, id):

    try:
        product = Product.objects.select_related('collection').get(id=id)
    except Product.DoesNotExist:
        return HttpResponse("Product not found")

    return HttpResponse(
        f"{product.title} - {product.collection.title} - ₹{product.unit_price}"
    )


# 9. Show all collections
def collection_list(request):

    collections = Collection.objects.all()

    result = ""

    for c in collections:
        result += f"{c.title}<br>"

    return HttpResponse(result)