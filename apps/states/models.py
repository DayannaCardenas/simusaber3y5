from django.db import models

# Create your models here.
class State(models.Model):
    name= models.CharField(max_length=20)

class StateTicket(models.Model):
    name= models.CharField(max_length=20)

