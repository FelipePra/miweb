from django.shortcuts import render
from django.http import JsonResponse

from apiApp.models import Alumno

# Create your views here.

def firstapi(request):
    alumnos = {
        #'id': 1,
        #'matricula': 202210151,
        #'nombre': 'Juan',
        #'apellido': 'Jara',
        #'email': 'jjara@inacapmai.cl',
        #'fono': '+569876543321'
    }
    lista = Alumno.objects.all()
    #transformar la lista de datos a Json
    data = {'alumnos':list(lista.values('matricula','nombre','apellido','email','fono'))}
    return JsonResponse(data)