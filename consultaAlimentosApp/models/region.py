from django.db import models

# nombre: no es unique ya que en dos paises puede haber regiones con nombres iguales
class Region(models.Model):
    id              = models.AutoField(primarykey=True)
    nombre          = models.CharField(max_length=60)
