from django.db import models
from .user     import User

class AlimentoTropical(models.Model):
	id 					= models.AutoField(primary_key = True)
	nombre				= models.CharField(max_length=150, unique=True)
	pesoPromUnidad  	= models.DecimalField(max_digits=5, decimal_places=2)
	grasaPromedio 		= models.DecimalField(max_digits=5, decimal_places=2)
	proteinaPromedio	= models.DecimalField(max_digits=5, decimal_places=2)
	carboPromedio 		= models.DecimalField(max_digits=5, decimal_places=2)
	vitaminaC			= models.BooleanField(default=False)
	vitaminaD			= models.BooleanField(default=False)
	hierro				= models.BooleanField(default=False)
	