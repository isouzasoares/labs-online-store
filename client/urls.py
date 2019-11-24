"""Client urls"""

from django.urls import path
from .views import ClientCreateView, ClientUpdateView

app_name = 'client'

urlpatterns = [
    path('create/', ClientCreateView.as_view(), name='create'),
    path('me/', ClientUpdateView.as_view(), name='update')
]
