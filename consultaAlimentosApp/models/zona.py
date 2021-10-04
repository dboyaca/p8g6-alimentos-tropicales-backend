from django.db import models
from .pais import Pais
from .region import Region

class Zona(models.Model):
    id              = models.AutoField(primary_key=True)
    id_pais            = models.ForeignKey(Pais,on_delete=models.CASCADE)
    id_region          = models.ForeignKey(Region,on_delete=models.CASCADE)
    