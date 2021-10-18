from rest_framework                                import serializers
from consultaAlimentosApp.models.region            import Region

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'nombre']

    def to_representation(self, obj):
        region = Region.objects.get(id = obj.id)

        return {
            'id'        : region.id,
            'nombre'    : region.nombre
        }