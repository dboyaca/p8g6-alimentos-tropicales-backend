from django.contrib import admin

from .models.user                   import User
from .models.alimentoTropical       import AlimentoTropical
from .models.cultivo                import Cultivo
from .models.pais                   import Pais
from .models.region                 import Region
from .models.zona                   import Zona

# Register your models here.

admin.site.register(User)
admin.site.register(AlimentoTropical)
admin.site.register(Cultivo)
admin.site.register(Pais)
admin.site.register(Region)
admin.site.register(Zona)

