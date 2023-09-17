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

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location, created = Location.objects.get_or_create(**location_data)
        product = Product.objects.create(location=location, **validated_data)
        return product
