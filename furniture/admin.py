from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'location',)
    list_filter = ('name', 'supplier', 'price', 'rating', 'quantity', 'location',)

admin.site.register(Product, ProductAdmin)
