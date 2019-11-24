"""Client urls"""

from django.urls import path
from .views import CustomerCreateView, CustomerRetrieveUpdateDestroyView

app_name = 'customer'

urlpatterns = [
    path('create/', CustomerCreateView.as_view(), name='create'),
    path('me/', CustomerRetrieveUpdateDestroyView.as_view(), name='crud')
]
