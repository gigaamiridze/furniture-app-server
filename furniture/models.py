from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Location(models.Model):
    country = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'{self.country}, {self.city}'

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    supplier = models.CharField(max_length=100, null=False, blank=False)
    image_url = models.CharField(max_length=300, null=False, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=False, blank=False)
    quantity = models.IntegerField(default=0, null=False, blank=False)
    description = models.TextField(validators=[MinLengthValidator(10), MaxLengthValidator(300)], null=False, blank=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
