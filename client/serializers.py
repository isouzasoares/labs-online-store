"""Django rest client serializers"""
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Client


class ClientBaseSerializer(serializers.ModelSerializer):
    """Serializer for user"""

    class Meta:
        model = Client
        fields = ("id", "name", "email",)


class ClientCreateSerializer(ClientBaseSerializer):
    """Serializer for create user"""
    email = serializers.EmailField(validators=[UniqueValidator(
        queryset=Client.objects.all(),
        message="There is already an account with this email")])

    class Meta:
        model = Client
        fields = ("id", "name", "email", "password")


class ClientUpdateSerializer(ClientBaseSerializer):
    """Serializer for user"""
    email = serializers.ReadOnlyField()
