"""Client urls"""

from django.urls import path
from .views import (CustomerCreateView, CustomerRetrieveUpdateDestroyView,
                    CustomerProductFavoriteView)

app_name = "customer"

urlpatterns = [
    path("create/", CustomerCreateView.as_view(), name="create"),
    path("me/", CustomerRetrieveUpdateDestroyView.as_view(), name="crud"),
    path("me/favorite/products",
         CustomerProductFavoriteView.as_view(), name="favorite_product"),
]
