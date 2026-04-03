from django.db.models import Count
from .filters import ProductFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .models import Product, Collection , Review
from .serializer import ProductSerializer, CollectionSerializer,ReviewSerializer
from orders.models import OrderItem


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['price', 'last_update']
    search_fields = ['title', 'description']

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

@api_view(['GET', 'POST'])
def collection_list(request):
    if request.method == 'GET':
        queryset = Collection.objects.annotate(product_count=Count('product')).all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, pk):
    collection = get_object_or_404(
        Collection.objects.annotate(product_count=Count('product')),
        pk=pk
    )

    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if collection.product_count > 0:
            return Response(
                {'error': 'Collection cannot be deleted because it has products.'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
