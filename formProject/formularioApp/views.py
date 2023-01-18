from django.shortcuts import render
from django.core.files import File

# Create your views here.

def information(request):
    data = {
        'titulo':'Informacion Master Template',
        'info': 'Sirve para poder cargar un template dentro de un maestro',
    }
    return render(request, 'info.html',data)

def registerName(request):
    #verifica si la peticion es Post
    if request.method == 'POST':
        #muestra el dato por la consola del servidor
        print(request.POST['nombre'])
        #abrimos el archivo con permiso de lectura y escritura
        f = open('info.txt', 'r+')
        #se lee el archivo avierto
        f.read()
        #abrir objeto para luego guardar la informacion captada
        archivo = File(f)
        archivo.write('Nombre:' + request.POST['nombre'])
    return render(request,'formulario.html')

def mostarDatos(request):
    f = open('info.txt', 'r')
    archivo = f.read()
    data = {'nombres' : archivo}
    return render(request,'lista.html',data)
    