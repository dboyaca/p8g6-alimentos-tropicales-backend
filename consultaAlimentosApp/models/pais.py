from django.db import models

class Pais(models.Model):
    id              = models.AutoField(primary_key=True)
    nombre          = models.CharField(max_length=60, unique=True)
    
