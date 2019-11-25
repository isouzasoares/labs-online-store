"""The product model"""
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    """Product model representation"""
    brand = models.CharField(max_length=150)
    title = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.URLField(max_length=200, null=True, blank=True)
    reviewScore = models.FloatField(default=0.0)
    created_at = models.DateTimeField(_("created at"), default=timezone.now)

    class Meta:
        ordering = ["brand"]

    def __str__(self):
        """Return str for object"""
        return self.title
