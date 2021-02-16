from django.db import models

# Create your models here.

class Product(models.Model):
	title		= models.CharField(max_length=120) # max_length is a required attribute
	description	= models.TextField()
	price		= models.DecimalField(decimal_places=2, max_digits=1000)
	summary		= models.TextField(default='This is cool!')
	featured	= models.BooleanField() # This field can't be empty, it must have some data, so...
										# you have 2 options, with different implications each one
										# null=True --> IT CAN'T BE EMPTY IN THE DATA BASE
										# blanck=False --> it means that is required (is has NOTHING to do with the db)
										# default=True --> ??? minute 57/58