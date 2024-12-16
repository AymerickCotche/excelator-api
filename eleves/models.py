from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Eleve(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    sexe = models.CharField(max_length=15)
    note = models.IntegerField()
    has_paid = models.BooleanField(default=False)
    value_paid = models.FloatField()
    paid_month = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]