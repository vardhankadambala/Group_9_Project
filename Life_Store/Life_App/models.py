from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class details(models.Model):
	fname= models.CharField(max_length=10)
	lname= models.CharField(max_length=10)
	phone_num=models.CharField(max_length=10,blank=True,null=True)
	age=models.CharField(max_length=10,blank=True,null=True)
	dob=models.DateField(blank=True,null=True)
	address= models.CharField(max_length=20,blank=True,null=True)
	email = models.EmailField()
	password = models.CharField(max_length=100)
	re_password = models.CharField(max_length=100)


	def __str__(self):
		return self.fname