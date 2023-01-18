"""apiProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from apiApp import views as a1
from serializerApp import views as a2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/alumnos/',a1.firstapi),
    path('api/alumnosser/',a2.lista_alumnos),
    path('createalumnos/',a2.create_alumnos,)
    path('detallealumnos/',a2.details_alumnos),
]
