""""Client views"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Client
from .serializer import ClientUpdateSerializer, ClientCreateSerializer


class ClientCreateView(generics.CreateAPIView):
    """Create client generic view"""
    serializer_class = ClientCreateSerializer

    def perform_create(self, serializer):
        """"Create user on django auth"""
        data = serializer.data
        data["username"] = data["name"]
        Client.objects.create_user(**data)


class ClientUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """Update client generic view"""
    permission_classes = [IsAuthenticated]
    serializer_class = ClientUpdateSerializer

    def get_object(self):
        """
        Returns authorized client.
        """
        obj = self.request.user
        self.check_object_permissions(self.request, obj)
        return obj
