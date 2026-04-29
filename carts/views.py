from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from .models import Cart
from .serializers import CartSerializer

class CartViewSet(CreateModelMixin, 
                  RetrieveModelMixin, 
                  DestroyModelMixin, 
                  GenericViewSet)
    
    queryset = Cart.objects.prefetch_related('cartitem_set__product').all()
    serializer_class = CartSerializer
