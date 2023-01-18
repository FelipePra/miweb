import imp
from django.shortcuts import render
from django.core.files import File

# Create your views here.

def plan(request):
    if request.method == 'POST':
        f = open('infoplanes.txt', 'r+')
        f.read()
        planes = File(f)
        texto = '<b>Run:</b>' + request.POST['run'] + '<br>'+'<b>Nombre:</b>' + request.POST['nombre'] + '<br>'+ '<b>Telefono:</b>' + request.POST['fono'] + '<br>'+ '<b>Email:</b>' + request.POST['mail'] + '<br>'+ '<b>Direccion:</b>' + request.POST['direccion'] + '<br>'+ '<b>Plan:</b>' + request.POST['planes'] + '<br>'+ '<b>Comentario:</b>' + request.POST['comentario']
        planes.write(texto)
    return render(request,'planes.html')

def datos(request):
    f = open('infoplanes.txt', 'r')
    texto = f.read()
    data = {'planes':texto}
    return render(request, 'MostrarDatos.html',data)