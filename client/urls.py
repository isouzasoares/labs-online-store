"""Client urls"""

from django.urls import path
from .views import ClientCreateView

app_name = 'client'

urlpatterns = [
    path('create/', ClientCreateView.as_view(), name='create')
]
