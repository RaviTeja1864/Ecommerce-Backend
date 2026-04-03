from django.http import HttpResponse
from .models import Order


def order_list(request):
    orders = Order.objects.select_related('customer').prefetch_related('orderitem_set__product')[:10]

    result = ""
    for order in orders:
        result += f"Order {order.id} — {order.customer}<br>"
        for item in order.orderitem_set.all():
            result += f"&nbsp;&nbsp;- {item.product.title} (qty: {item.quantity})<br>"

    return HttpResponse(result)
