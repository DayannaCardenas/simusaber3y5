from django.db import models
from apps.states.models import *
from apps.profiles.models import *

# Create your models here.
class TypeProduct(models.Model):
    name = models.CharField(max_length=50)

class TypeIncidence(models.Model):
    name = models.CharField(max_length=50)

class Aspect(models.Model):
    name = models.CharField(max_length=50)

class Priority(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to = 'priority_image')

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    state = models.ForeignKey(State, on_delete = models.CASCADE, null=True)
    image = models.ImageField(upload_to = 'product_image')
    type_product = models.ForeignKey(TypeProduct, on_delete = models.CASCADE, null=True)
    version = models.CharField(max_length=10)

class Ticket(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null=True)
    type_incidence = models.ForeignKey(TypeIncidence, on_delete = models.CASCADE, null=True)
    aspect = models.ForeignKey(Aspect, on_delete = models.CASCADE, null=True)
    description = models.TextField()
    
class MediaTicket(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete = models.CASCADE, null=True)
    file_media = models.FileField(upload_to = 'mediaticket_file', null=True)

