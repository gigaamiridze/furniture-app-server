from rest_framework.serializers import ModelSerializer
from .models import Product, Location

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ['country', 'city']

class ProductSerializer(ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Product
        fields = '__all__'
