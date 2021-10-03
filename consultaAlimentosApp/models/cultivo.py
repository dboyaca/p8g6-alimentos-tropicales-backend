from django.db         import models
from .alimentoTropical import AlimentoTropical
from .zona             import Zona

class AlimentoTropical(models.Model):
    id                      = models.AutoField(primarykey=True)
    alimentoSembrado        = models.ForeignKey(AlimentoTropical, on_delete=models.CASCADE, on_update=models.CASCADE)
    zonaCultivo             = models.ForeignKey(Zona, on_delete=models.CASCADE, on_update=models.CASCADE)
    hectareas               = models.DecimalField(max_digits=5, decimalplaces=2)
    fecha                   = models.DateField(auto_now_add=True)
