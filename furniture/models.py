from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    supplier = models.CharField(max_length=100, null=False, blank=False)
    image_url = models.CharField(max_length=300, null=False, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=False, blank=False)
    quantity = models.IntegerField(default=0, null=False, blank=False)
    description = models.TextField(validators=[MinLengthValidator(10), MaxLengthValidator(300)], null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
