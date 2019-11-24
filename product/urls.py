"""Product urls"""

from django.urls import path
from .views import GetProductView, ListProductView

app_name = 'product'

urlpatterns = [
    path('', ListProductView.as_view(), name='list'),
    path('<pk>', GetProductView.as_view(), name='get')
]
