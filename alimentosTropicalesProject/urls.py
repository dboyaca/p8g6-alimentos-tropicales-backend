"""alimentosTropicalesProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from consultaAlimentosApp import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()), #SW que me da los tokens de acceso y de refresh pal usuario
    path('refresh/', TokenRefreshView.as_view()), #Refrescamos el token de acceso con esta vista
    path('user/', views.userCreateView.UserCreateView.as_view()),
    path('user/<int:pk>/', views.userDetailView.UserDetailView.as_view()),
    path('cultivo/create/', views.cultivoCreateView.CultivoCreateView.as_view()),
    path('cultivo/<int:user>/<int:pk>/', views.cultivoRUDView.CultivoDetailView.as_view()),
    path('cultivo/<int:user>/', views.cultivoRUDView.CultivosView.as_view())
]
