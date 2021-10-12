from django.conf                                                import settings
from rest_framework                                             import generics, status
from rest_framework.response                                    import Response
from rest_framework.permissions                                 import IsAuthenticated
from rest_framework_simplejwt.backends                          import TokenBackend

from consultaAlimentosApp.models.pais                           import Pais
from consultaAlimentosApp.models.region                         import Region
from consultaAlimentosApp.models.zona                           import Zona

from consultaAlimentosApp.serializers.cultivoSerializers import CultivoSerializer

'''Recuerde que aquí le tengo que enviar en la URL el parámetro de filtro'''
class CultivoCreateView(generics.CreateAPIView):
    serializer_class                = CultivoSerializer
    permission_classes              = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        #Provenientes de una drop-down list 
        pais    = request.data['transaction_data']['pais']
        region  = request.data['transaction_data']['region']

        #Ni el país ni la región están registrados en el sistema
        if pais == 1 and region == 1:
            codigo_pais     = Pais.objects.create(
                nombre=request.data['transaction_data']['nombrePais'])

            codigo_region   = Region.objects.create(
                                nombre=request.data['transaction_data']['nombreRegion'])

            codigo_zona     = Zona.objects.create(id_pais=codigo_pais, id_region=codigo_region)

            request.data['transaction_data']['pais']        = codigo_pais.id
            request.data['transaction_data']['region']      = codigo_region.id

            request.data['transaction_data']['zonaCultivo'] = codigo_zona.id

        #La región no está registrada en el sistema pero el país sí
        elif pais != 1 and region == 1:
            
            #codigo_pais     = Pais.objects.get(id=request.data['transaction_data']['pais'])
            
            codigo_region   = Region.objects.create(
                                nombre=request.data['transaction_data']['nombreRegion'])

            codigo_zona     = Zona.objects.create(
                                id_pais=Pais.objects.get(id=request.data['transaction_data']['pais']),
                                id_region=codigo_region )

            request.data['transaction_data']['region']      = codigo_region.id
            request.data['transaction_data']['zonaCultivo'] = codigo_zona.id

        #Tanto la región como el país están registradas en el sistema
        elif pais != 1 and region != 1:
            codigo_zona = Zona.objects.create(
                            id_pais   = Pais.objects.get(id=request.data['transaction_data']['pais']),
                            id_region = Region.objects.get(id=request.data['transaction_data']['region'])).id

            request.data['transaction_data']['zonaCultivo'] = codigo_zona

            print(request.data)
            

        #Borramos campos adicionales que no deberían ir a la creación de un objeto del modelo
        request.data['transaction_data'].pop('nombrePais')
        request.data['transaction_data'].pop('nombreRegion')
        print(request.data)

        serializer = CultivoSerializer(data=request.data['transaction_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Transacción exitosa", status=status.HTTP_201_CREATED)