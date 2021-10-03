from django.db import models
from .pais import Pais
from .region import Region

class Zona(models.Model):
    id              = models.AutoField(primarykey=True)
    pais            = models.ForeignKey(Pais,on_delete=models.CASCADE, on_update=models.CASCADE)
    region          = models.ForeignKey(Region,on_delete=models.CASCADE, on_update=models.CASCADE)
    