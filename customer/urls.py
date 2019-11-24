"""Client urls"""

from django.urls import path
from .views import CustomerCreateView, CustomerUpdateView

app_name = 'customer'

urlpatterns = [
    path('create/', CustomerCreateView.as_view(), name='create'),
    path('me/', CustomerUpdateView.as_view(), name='crud')
]
