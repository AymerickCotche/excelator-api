from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ["-created"]

class Sale(models.Model):
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')

    class Meta:
        ordering = ["-created"]

class Purchase(models.Model):
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchases')

    class Meta:
        ordering = ["-created"]