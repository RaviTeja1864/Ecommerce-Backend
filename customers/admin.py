from django.contrib import admin
from django.db.models import Count
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'membership', 'orders_count']

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(orders_count=Count('order'))

    def orders_count(self, customer):
        return customer.orders_count

    orders_count.short_description = 'Orders'
