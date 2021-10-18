from consultaAlimentosApp.models.alimentoTropical   import AlimentoTropical
from rest_framework                                 import serializers

class AlimentoTropicalSerializer(serializers.ModelSerializer):

    """--Esta parte me traduce de JSON a Modelo"""
    class Meta: 
        model = AlimentoTropical
        fields = ['id', 'nombre', 'pesoPromUnidad','grasaPromedio','proteinaPromedio',
                'carboPromedio','vitaminaC','vitaminaD','hierro']

    """--Acá me traduce del modelo al JSON"""
    """--obj: Objeto del modelo a serializar"""
    def to_representation(self, obj):
        
        alimentoTropical = AlimentoTropical.objects.get(id=obj.id)

        return {
            "id"                : alimentoTropical.id,
            "nombre"            : alimentoTropical.nombre
        }



            








