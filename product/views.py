""""Product views"""

from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ListProductView(generics.ListAPIView):
    """Generic view for product list"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class GetProductView(generics.RetrieveAPIView):
    """Generic view for product detail"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
