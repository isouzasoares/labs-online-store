""""Product views"""

from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ListProductView(generics.ListAPIView):
    """Lists all products registered in django admin"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class GetProductView(generics.RetrieveAPIView):
    """Get the product detail"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
