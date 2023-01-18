from django.shortcuts import render

from apiApp.models import Alumno
from serializerApp.serializers import AlumnoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    ser = AlumnoSerializer(alumnos, many=True)
    return Response(ser.data)

@api_view(['POST'])
def create_alumnos(request):
    if request.method == 'POST':
        #Pasamos la data enviada por Post al serializer
        ser = AlumnoSerializer(data=request.data)
        #Si la informacion enviada es valida
        if ser.is_valid():
            if not ser.validar_matricula(request.data('matricula')):
                #Se guarda en la DB
                ser.save()
                return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.data,status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def details_alumnos(request,id):
    
        alumno = Alumno.objects.get(id=id)

        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        ser = AlumnosSerializer(alumno)
        return Response(ser,data)

