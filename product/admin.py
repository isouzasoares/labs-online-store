"""Django active admin"""

from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    """Product admin representation"""
    list_filter = ('brand',)
    list_display = ('title', 'brand', 'price')
    ordering = ['created_at']
    search_fields = ['title']


admin.site.register(Product, ProductAdmin)
