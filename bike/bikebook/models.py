from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Address(models.Model):
	firstname = models.CharField(max_length=32)
	lastname = models.CharField(max_length=32)
	username = models.CharField(max_length=32)
	emailid = models.CharField(max_length=60)
	address = models.CharField(max_length=60)
	pincode = models.IntegerField()
	age = models.IntegerField()
	

class Addbike(models.Model):
	brands = [('honda',"honda"),('royalenfield',"royalenfield"),('bmw',"bmw")]
	bikes = [('Spshine',"Spshine"),('Hornet',"Hornet"),('Xblade',"Xblade"),('Navi',"Navi"),('Royal Enfield Classic 350',"Royal Enfield Classic 350"),('Royal Enfield Himalayan',"Royal Enfield Himalayan"),('Royal Enfield Continental GT',"Royal Enfield Continental GT"),('Royal Enfield Interceptor 650',"Royal Enfield Interceptor 650"),('BMW G310R',"BMW G310R"),('BMW S1000 RR',"BMW S1000 RR"),('BMW R1250 GS',"BMW R1250 GS"),('BMW R nine T',"BMW R nine T")]
	brandname = models.CharField(max_length=20,choices=brands)
	brandlogo = models.ImageField(upload_to = "brands/")
	bikemodel = models.CharField(max_length=60,choices=bikes)
	bikefrontimage = models.ImageField(upload_to="bikes/")
	bikebackimage = models.ImageField(upload_to="bikes/")
	bikeleftimage = models.ImageField(upload_to="bikes/")
	bikerightimage = models.ImageField(upload_to="bikes/")
	bikecost = models.IntegerField()
	bikecc = models.IntegerField()
	injection = [('bs4',"bs4"),('bs6',"bs6")]
	fuelinjectiontype = models.CharField(max_length=10,choices=injection) 
	location = models.CharField(max_length=30)

