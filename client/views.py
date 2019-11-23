""""Client views"""

from rest_framework import generics
from .serializer import ClientCreateSerializer


class ClientCreateView(generics.CreateAPIView):
    """Create client generic view"""
    serializer_class = ClientCreateSerializer
