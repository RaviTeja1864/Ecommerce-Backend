from django.shortcuts import render
from store.models import Product
from django.http import HttpResponse
from .models import Collection
from django.db.models import Count

#select_related
def product_list(request):
    products = Product.objects.select_related('collection').all()

    return render(request, 'products.html', {'products': products})

#prefetech_related
def collections_products(request):
    collections = Collection.objects.prefetch_related('product_set')

    result = ""

    for c in collections:
        for p in c.product_set.all():
            result += f"{c.title} → {p.title}<br>"

    return HttpResponse(result)


#annotate
def collections_with_product_count(request):

    collections = Collection.objects.annotate(
        product_count=Count('product')
    )

    result = ""

    for c in collections:
        result += f"{c.title} - {c.product_count} products<br>"

    return HttpResponse(result)

#values
def product_titles_prices(request):

    products = Product.objects.values('title', 'unit_price')[:10]

    result = ""

    for p in products:
        result += f"{p['title']} - {p['unit_price']}<br>"

    return HttpResponse(result)

#values_list
def product_titles_prices_list(request):

    products = Product.objects.values_list('title', 'unit_price')[:10]

    result = ""

    for title, price in products:
        result += f"{title} - {price}<br>"

    return HttpResponse(result)