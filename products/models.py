from django.db import models
from django.utils import timezone
from datetime import timedelta
from pages.models import BaseModel


class ProductModel(BaseModel):
    name = models.CharField(max_length=255)
    reference = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def is_new(self):
        return timezone.now() - self.created_at <= timedelta(days=3)

    def __str__(self):
        return self.name
