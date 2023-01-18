from dataclasses import dataclass
from typing import TextIO
from django.shortcuts import render
from django.core.files import File
# Create your views here.

def create(request):
    if request.method == 'POST':
        f= open('empleado.txt','r+')
        f.read()
        empleado = File(f)
        texto = '<b>Run:</b>' + request.POST['run'] + '<b>Nombre:</b>' + request.POST['nombre'] + '<b>Fecha Nacimiento:</b>' + request.POST['fecha'] + '<b>Estado Civil:</b>' + request.POST['ecivil'] + '<b>Genero:</b>' + request.POST['genero'] + '<b>Comentario:</b>' + request.POST['comentario']
        empleado.write(texto)
    return render(request,'create.html')

def list(request):
    f= open('empleado.txt', 'r')
    texto = f.read()
    data = {'empleados': texto}
    return render(request, 'list.html',data)