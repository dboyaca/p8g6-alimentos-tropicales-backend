from django.db         import models
from .alimentoTropical import AlimentoTropical
from .zona             import Zona

class Cultivo(models.Model):
    id                      = models.AutoField(primary_key=True)
    alimentoSembrado        = models.ForeignKey(AlimentoTropical, on_delete=models.CASCADE)
    zonaCultivo             = models.ForeignKey(Zona, on_delete=models.CASCADE)
    hectareas               = models.DecimalField(max_digits=5, decimal_places=2)
    fecha                   = models.DateField(auto_now_add=True)

    def getId(self):
        return self.id

    def getAlimentoSembrado(self):
        return int(self.alimentoSembrado)