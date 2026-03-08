from django.shortcuts import render
from django.http import HttpResponse
from .models import Order

def order_list(request):
    orders = Order.objects.prefetch_related('orderitem_set')[:10]

    result = ""
    for order in orders:
        result += f"Order {order.id}<br>"
        for item in order.orderitem_set.all():
            result += f"- {item.product.title} ({item.quantity})<br>"

    return HttpResponse(result)

