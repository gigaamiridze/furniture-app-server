from django.contrib import admin
from .models import Product, Location

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'location',)
    list_filter = ('name', 'supplier', 'price', 'rating', 'quantity', 'location',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('country', 'city',)
    list_filter = ('country', 'city',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Location, LocationAdmin)
