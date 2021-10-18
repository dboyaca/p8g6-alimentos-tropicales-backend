from rest_framework                               import serializers
from consultaAlimentosApp.models.pais             import Pais

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['id', 'nombre']

    def to_representation(self, obj):
        pais = Pais.objects.get(id = obj.id)

        return {
            'id'        : pais.id,
            'nombre'    : pais.nombre
        }