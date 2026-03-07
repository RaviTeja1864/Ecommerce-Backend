from django.contrib import admin
from .models import Collection, Product

admin.site.register(Collection)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','inventory','collection']
    search_fields = ['title']
    list_filter = ['collection']
    list_per_page = 10
