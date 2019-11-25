"""Django rest client serializers"""
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Customer, CustomerFavoriteProduct


class CustomerBaseSerializer(serializers.ModelSerializer):
    """Serializer for user"""

    class Meta:
        model = Customer
        fields = ("id", "name", "email")


class CustomerCreateSerializer(CustomerBaseSerializer):
    """Serializer for create user"""

    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=Customer.objects.all(),
                message="There is already an account with this email",
            )
        ]
    )

    class Meta:
        model = Customer
        fields = ("id", "name", "email", "password")


class CustomerUpdateSerializer(CustomerBaseSerializer):
    """Serializer for user"""

    email = serializers.ReadOnlyField()


class CustomerFavoriteProductSerializer(serializers.ModelSerializer):
    """Serializer for customer product favorite"""

    created_at = serializers.ReadOnlyField()

    class Meta:
        model = CustomerFavoriteProduct
        fields = ("product", "price", "created_at",)
