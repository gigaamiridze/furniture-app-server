from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('products', views.get_products, name='products'),
    path('products/<int:pk>', views.get_product, name='product'),
    path('create-product', views.create_product, name='create_product'),
    path('search/<str:key>', views.search_product, name='search_product'),
]
