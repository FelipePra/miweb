from django.shortcuts import render

from especieApp.forms import FormEspecie
from especieApp.models import Especie

# Create your views here.

def createespecie (request):
    form = FormEspecie()
    if request.method == 'POST':
        form = FormEspecie(request.POST)
        if form.is_valid():
            form.save()
            return listaespecie(request)    
    data = {'form':form,'titulo':'Ingresar Especie'}
    return render(request, 'create.html',data)

def listaespecie (request):
    lista = Especie.objects.all()
    data = {'especie' : lista}
    return render(request, 'Index.html',data)