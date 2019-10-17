from django.db import models

# Create your models here.
class student(models.Model):
	name 			= models.CharField(max_length=50)
	rollnumber  	= models.CharField(max_length=22)
	service		    = models.CharField(max_length=50)
