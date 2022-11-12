from django.db import models
from apps.states.models import *

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)

class Departament(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete = models.CASCADE, null=True)

class City(models.Model):
    name = models.CharField(max_length=50)
    departament = models.ForeignKey(Departament, on_delete = models.CASCADE, null=True)

class Office(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete = models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete = models.CASCADE, null=True)
    image = models.ImageField(upload_to = 'office_image')