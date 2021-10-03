from django.db import models
from .user     import User

class AlimentoTropical(models.Model):
	id 					= models.AutoField(primarykey = True)
	nombre				= models.CharField(max_length=150, unique=True)
	imagen  			= models.FileField()
	pesoPromUnidad  	= models.DecimalField(max_digits=5, decimalplaces=2)
	grasaPromedio 		= models.DecimalField(max_digits=5, decimalplaces=2)
	proteinaPromedio	= models.DecimalField(max_digits=5, decimalplaces=2)
	carboPromedio 		= models.DecimalField(max_digits=5,decimalplaces=2)
	vitaminaC			= models.BooleanField(default=False)
	vitaminaD			= models.BooleanField(default=False)
	hierro				= models.BooleanField(default=False)