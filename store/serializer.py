from rest_framework import serializers
from decimal import Decimal
from .models import Product, Collection, Review


class CollectionSerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Collection
        fields = ['id', 'title', 'product_count']


class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'price_with_tax', 'description', 'inventory', 'collection']

    def calculate_tax(self, product: Product):
        return product.price * Decimal(1.1)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description','date']