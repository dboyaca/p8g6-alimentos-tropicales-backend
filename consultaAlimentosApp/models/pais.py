from django.db import models
from .pais import Pais
from .region import Region

class Zona(models.Model):
    id              = models.AutoField(primarykey=True)
    nombre          = models.CharField(max_length=60, unique=True)
    
