"""Django rest product serializers"""
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for product"""

    class Meta:
        model = Product
        fields = "__all__"
