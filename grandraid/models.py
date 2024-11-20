from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Club(models.Model):
    name = models.CharField()
    adress = models.TextField()
    zip_code = models.IntegerField()
    city = models.CharField()
    ffa_number = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

class Course(models.Model):
    name = models.CharField()
    price = models.FloatField()
    has_discount = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

class Size(models.Model):
    name = models.CharField()
    symbol = models.CharField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]

class RunnerCategory(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    category = models.CharField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["start_year"]

class Meal(models.Model):
    type = models.CharField()
    prix = models.IntegerField()
    name = models.CharField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

class Runner(models.Model):
    firstname = models.TextField(max_length=20)
    lastname = models.TextField(max_length=20)
    class Sexe(models.TextChoices):
        HOMME = "H", _("Homme")
        FEMME = "F", _("Femme")
    sexe = models.CharField(
        max_length=1,
        choices=Sexe,
        default=Sexe.FEMME,
    )
    birth_date = models.DateField()
    category = models.TextField()
    shirt_size = models.ForeignKey(Size, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    meal_before = models.BooleanField(default=False)
    meal_after = models.BooleanField(default=False)