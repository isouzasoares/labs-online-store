""""Client views"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Customer
from .serializers import CustomerUpdateSerializer, CustomerCreateSerializer


class CustomerCreateView(generics.CreateAPIView):
    """Create client generic view"""
    serializer_class = CustomerCreateSerializer

    def perform_create(self, serializer):
        """"Create user on django auth"""
        data = serializer.data
        data["username"] = data["name"]
        Customer.objects.create_user(**data)


class CustomerUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """Update client generic view"""
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerUpdateSerializer

    def get_object(self):
        """
        Returns authorized client.
        """
        obj = self.request.user
        self.check_object_permissions(self.request, obj)
        return obj
