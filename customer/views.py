""""Client views"""

from rest_framework import generics
from rest_framework.serializers import PrimaryKeyRelatedField
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from product.serializers import ProductSerializer
from product.models import Product
from .models import Customer
from .serializers import (CustomerUpdateSerializer, CustomerCreateSerializer,
                          CustomerFavoriteProductSerializer)


class CustomerCreateView(generics.CreateAPIView):
    """Create client generic view"""

    serializer_class = CustomerCreateSerializer

    def perform_create(self, serializer):
        """"Create user on django auth"""
        data = serializer.data
        data["username"] = data["name"]
        Customer.objects.create_user(**data)


class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
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


class CustomerProductFavoriteView(generics.ListCreateAPIView):
    """Post or list product favorites generic view"""

    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        """
        Create queryset for customer
        """
        qs = super().get_queryset()
        return qs.filter(customerfavoriteproduct__customer=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Delete or create favorite for customer
        If delete return 204 else 201
        """
        data = request.data
        data["customer"] = request.user.pk
        serializer = CustomerFavoriteProductSerializer(data=data)
        serializer.fields["customer"] = PrimaryKeyRelatedField(
            queryset=Customer.objects.filter(pk=request.user.pk))
        serializer.is_valid(raise_exception=True)
        user_product = request.user.customerfavoriteproduct_set.filter(
            product_id=serializer.validated_data["product"])
        if not user_product:
            self.perform_create(serializer)
            http_status = status.HTTP_201_CREATED
        else:
            user_product.delete()
            http_status = status.HTTP_204_NO_CONTENT
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=http_status,
                        headers=headers)
