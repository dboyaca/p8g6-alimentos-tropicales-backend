from rest_framework                                               import serializers

from consultaAlimentosApp.models.cultivo                          import Cultivo
from consultaAlimentosApp.models.alimentoTropical                 import AlimentoTropical
from consultaAlimentosApp.serializers.alimentoTropicalSerializers import AlimentoTropicalSerializer
from django.db                                                    import connection


#---------------------------------------------------------------------------------
#                        Funciones para consulta pura SQL        
#---------------------------------------------------------------------------------

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

"""Query diseñado para traer el pais y la región en la que está establecida un cultivo sin necesidad
    de pasar por la tabla zona"""
def custom_sql(idCultivo):
    with connection.cursor() as cursor:
            sql = "SELECT Cultivo.id, Pais.nombre AS pais, Region.nombre AS region, Zona.id AS zona \
                    FROM consultaalimentosapp_cultivo AS Cultivo \
                    JOIN consultaalimentosapp_zona AS Zona ON Cultivo.zonaCultivo_id = Zona.id \
                    JOIN consultaalimentosapp_pais AS Pais ON Zona.id_pais_id = Pais.id  \
                    JOIN consultaalimentosapp_region AS Region ON Zona.id_region_id = Region.id \
                    WHERE Cultivo.id = %s;"
            cursor.execute(sql, ((idCultivo), ))
            resultSet = dictfetchall(cursor) # [{'id': 9, 'pais': 'Colombia', 'region': 'Boyacá'}]
    return resultSet[0]

#---------------------------------------------------------------------------------
#                               CultivoSerializer      
#---------------------------------------------------------------------------------

class CultivoSerializer(serializers.ModelSerializer):
    #alimento_tropical = AlimentoTropicalSerializer() #Acá estaba el fallo
    class Meta:
        model = Cultivo
        fields = ['id', 'alimentoSembrado','hectareas','fecha','zonaCultivo']

    def to_representation(self, obj):
        cultivo = Cultivo.objects.get(id = obj.id)
        alimento_tropical = AlimentoTropical.objects.get(id=cultivo.alimentoSembrado.id)
        datosZona = custom_sql(obj.id)

        return {
            'id' : cultivo.id,
            'alimento_sembrado' : {
                'id_alimento'   : alimento_tropical.id,
                'nombre'        : alimento_tropical.nombre,
                'proteina'      : alimento_tropical.proteinaPromedio,
                'grasa'         : alimento_tropical.grasaPromedio,
                'carbohidratos' : alimento_tropical.carboPromedio,
            },         
            'hectareas'     : cultivo.hectareas,
            'fecha'         : cultivo.fecha,
            'zonaCultivo'       : {
                'zona'          : datosZona['zona'],
                'pais'          : datosZona['pais'],
                'region'        : datosZona['region']
            }
        }
