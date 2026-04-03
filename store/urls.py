from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('products', views.ProductViewSet)

urlpatterns = router.urls + [
    path('collections/', views.collection_list, name='collection-list'),
    path('collections/<int:pk>/', views.collection_detail, name='collection-detail'),
]
