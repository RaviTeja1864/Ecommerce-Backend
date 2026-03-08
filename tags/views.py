from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def product_tags(request):
    products = Product.objects.prefetch_related('taggeditem_set')[:10]

    result = ""
    for p in products:
        result += f"{p.title}<br>"
        for tag in p.taggeditem_set.all():
            result += f"- {tag.tag}<br>"

    return HttpResponse(result)

