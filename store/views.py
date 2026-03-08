from django.shortcuts import render
from.models import Product
from django.http import HttpResponse
def product_list(request):
    products = Product.objects.select_related('collection').all()[:20]

    result = ""
    for p in products:
        result += f"{p.title} - {p.collection.title}<br>"

    return HttpResponse(result)   
