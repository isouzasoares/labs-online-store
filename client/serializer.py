"""Django rest client serializers"""
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Client


class ClientCreateSerializer(serializers.ModelSerializer):
    """Serializer for create user"""
    email = serializers.EmailField(validators=[UniqueValidator(
        queryset=Client.objects.all(),
        message="There is already an account with this email")])

    class Meta:
        model = Client
        exclude = ("is_staff", "is_superuser", "date_joined",)
