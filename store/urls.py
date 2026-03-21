from django.urls import path
from . import views

urlpatterns = [

    path('products/', views.product_list),

    path('product/<int:id>/', views.product_detail),

    path('collections/<int:pk>/', views.collection_detail,name ='collection-detail'),

    path('collections-products/', views.collections_products),

    path('collections-count/', views.collections_with_product_count),

    path('values-products/', views.product_titles_prices),

    path('valueslist-products/', views.product_titles_prices_list),

    path('cheap-products/', views.cheap_or_high_inventory),

    path('increase-inventory/', views.increase_inventory),
]