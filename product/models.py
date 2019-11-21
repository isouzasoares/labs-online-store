"""The product model"""
from django.db import models


class Product(models.Model):
    brand = models.CharField(max_length=150)
    title = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.URLField(max_length=200, null=True, blank=True)
    reviewScore = models.FloatField(default=0.0)
