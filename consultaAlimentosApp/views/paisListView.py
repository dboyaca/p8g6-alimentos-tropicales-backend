from django.conf                                                import settings
from rest_framework                                             import generics, status
from rest_framework.response                                    import Response
from rest_framework.permissions                                 import IsAuthenticated
from rest_framework_simplejwt.backends                          import TokenBackend

from consultaAlimentosApp.models.pais                           import Pais
from consultaAlimentosApp.serializers.paisSerializers           import PaisSerializer

class PaisesView(generics.ListAPIView): #Hace más uso de la abstracción q Retrieve
    serializer_class   = PaisSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Pais.objects.all()

        return queryset