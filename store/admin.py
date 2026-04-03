from django.contrib import admin
from .models import Collection, Product


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory', 'collection']
    search_fields = ['title']
    list_filter = ['collection']
    list_per_page = 10
