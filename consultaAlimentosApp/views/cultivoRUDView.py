from django.conf                                                import settings
from rest_framework                                             import generics, status
from rest_framework.response                                    import Response
from rest_framework.permissions                                 import IsAuthenticated
from rest_framework_simplejwt.backends                          import TokenBackend


from consultaAlimentosApp.models.cultivo                        import Cultivo
from consultaAlimentosApp.serializers.cultivoSerializers        import CultivoSerializer

class CultivoDetailView(generics.RetrieveAPIView):
    serializer_class   = CultivoSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Cultivo.objects.all()

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)


class CultivosView(generics.ListAPIView): #Hace más uso de la abstracción q Retrieve
    serializer_class   = CultivoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Cultivo.objects.all()

        return queryset

