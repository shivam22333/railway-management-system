from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator,MaxLengthValidator,MaxValueValidator, MinValueValidator
from django.core import validators

class Register(models.Model):
	name=models.CharField(validators=[MinLengthValidator(1)],max_length=20,null=True,blank=True)
	username=models.CharField(validators=[MinLengthValidator(1)],max_length=20,null=True,blank=True)
	mobile=models.IntegerField(null=True,blank=True)
	email=models.EmailField(null=True,blank=True)
	password=models.CharField(validators=[MinLengthValidator(8)],max_length=50,null=True,blank=True)
	

	def __str__(self):
		return str(self.name)

class Station(models.Model):
	station=models.CharField(max_length=50,null=True)

	def __str__(self):
		return str(self.station)

class Train(models.Model):
	name=models.CharField(max_length=50,null=True)
	no=models.IntegerField(null=True)
	arrival=models.TimeField(null=True)
	departure=models.TimeField(null=True)
	dest_1=models.ForeignKey(Station,on_delete=models.CASCADE,null=True,related_name='des')
	dest_2=models.ForeignKey(Station,on_delete=models.CASCADE,null=True)
	tsc=models.IntegerField(null=True)
	sc=models.IntegerField(null=True)
	sc_price=models.IntegerField(null=True)
	tfirst_ac=models.IntegerField(null=True)
	first_ac=models.IntegerField(null=True)
	first_price=models.IntegerField(null=True)
	tsecond_ac=models.IntegerField(null=True)
	second_ac=models.IntegerField(null=True)
	second_price=models.IntegerField(null=True)
	tthird_ac=models.IntegerField(null=True)
	third_ac=models.IntegerField(null=True)
	third_price=models.IntegerField(null=True)

	def __str__(self):
		return str(self.name)

class Detail(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	train=models.ForeignKey(Train,on_delete=models.CASCADE,null=True,blank=True)
	coach=models.CharField(max_length=50,null=True,blank=True)#from ,to, arrival, departure
	coach_train=models.CharField(max_length=50,null=True,blank=True)
	book_date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
	pnr=models.PositiveIntegerField(null=True,blank=True)
	date=models.CharField(max_length=50,null=True,blank=True)
	passenger1=models.CharField(max_length=50,null=True,blank=True)
	gender1=models.CharField(max_length=50,null=True,blank=True)
	age1=models.PositiveIntegerField(null=True,blank=True)
	seat1=models.PositiveIntegerField(null=True,blank=True)
	passenger2=models.CharField(max_length=50,null=True,blank=True)
	gender2=models.CharField(max_length=50,null=True,blank=True)
	age2=models.PositiveIntegerField(null=True,blank=True)
	seat2=models.PositiveIntegerField(null=True,blank=True)
	passenger3=models.CharField(max_length=50,null=True,blank=True)
	gender3=models.CharField(max_length=50,null=True,blank=True)
	age3=models.PositiveIntegerField(null=True,blank=True)
	seat3=models.PositiveIntegerField(null=True,blank=True)
	passenger4=models.CharField(max_length=50,null=True,blank=True)
	gender4=models.CharField(max_length=50,null=True,blank=True)
	age4=models.PositiveIntegerField(null=True,blank=True)
	seat4=models.PositiveIntegerField(null=True,blank=True)
	amount=models.FloatField(null=True,blank=True)


class Contact(models.Model):
	name=models.CharField(max_length=50,null=True,blank=True)
	email=models.EmailField(null=True,blank=True)
	message=models.TextField(max_length=500,null=True,blank=True)