from django.db import models
from django.contrib.auth.models import *
from apps.states.models import *
from apps.locations.models import *

# Create your models here.
class CodeVerify(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	code = models.CharField(max_length=6)
	state = models.ForeignKey(State, on_delete = models.CASCADE, null=True)
	def __str__(self):
		return '{}'.format(self.user)

class TypeFuncionary(models.Model):
	name = models.CharField(max_length=50)

class TypeDocument(models.Model):
	name = models.CharField(max_length=10)

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	type_document = models.ForeignKey(TypeDocument, on_delete = models.CASCADE, null=True)
	document = models.CharField(max_length=50)
	cell_phone = models.CharField(max_length=20)
	phone = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	state = models.ForeignKey(State, on_delete = models.CASCADE, null=True, default=1)
	office = models.ForeignKey(Office, on_delete = models.CASCADE, null=True)
	image = models.ImageField(upload_to = 'customer_image')
	url = models.CharField(max_length=100)

class Funcionary(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	type_document = models.ForeignKey(TypeDocument, on_delete = models.CASCADE, null=True)
	document = models.CharField(max_length=50)
	cell_phone = models.CharField(max_length=20)
	phone = models.CharField(max_length=20)
	image = models.ImageField(upload_to = 'funcionary_image')
	state = models.ForeignKey(State, on_delete = models.CASCADE, null=True, default=1)
	type_funcionary = models.ForeignKey(TypeFuncionary, on_delete = models.CASCADE, null=True)
	customer = models.ForeignKey(Customer, on_delete = models.CASCADE, null=True)
	address = models.CharField(max_length=100)

class HelpDesk(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	type_document = models.ForeignKey(TypeDocument, on_delete = models.CASCADE, null=True)
	document = models.CharField(max_length=50)
	cell_phone = models.CharField(max_length=20)
	state = models.ForeignKey(State, on_delete = models.CASCADE, null=True, default=1)
	image = models.ImageField(upload_to = 'helpdesk_image')

class Connection(models.Model):
	user_1 = models.ForeignKey(User, on_delete = models.CASCADE, null=False,related_name='user_1')
	user_2 = models.ForeignKey(User, on_delete = models.CASCADE, null=False,related_name='user_2')

class Message(models.Model):
	connection = models.ForeignKey(Connection, on_delete = models.CASCADE)
	content =models.TextField()
	transmitter = models.ForeignKey(User, on_delete = models.CASCADE)
	date = models.DateTimeField(null=False,default=timezone.now)
	flag = models.BooleanField(null=False,default=True)


