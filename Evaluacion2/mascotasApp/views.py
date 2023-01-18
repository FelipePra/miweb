from django.shortcuts import redirect, render

from mascotasApp.forms import FormMascota
from mascotasApp.models import Mascota

# Create your views here.

def createmascota(request):
    form = FormMascota()
    if request.method == 'POST':
        form = FormMascota(request.POST)
        if form.is_valid():
            form.save()
            return listamascota(request)    
    data = {'form':form,'titulo':'Crear Mascota'}
    return render(request, 'create.html',data)

def listamascota (request):
    lista = Mascota.objects.all()
    data = {'mascota' : lista}
    return render(request, 'IndexMascota.html',data)

#metodo para eliminar
def eliminarmascota(request,id):
    mascota = Mascota.objects.get(id = id)
    mascota.delete()
    return redirect('/listamascota')

def editarmascota(request,id):
    per = Mascota.objects.get(id=id)
    form = FormMascota(instance=per)
    if request.method == 'POST':
        form = FormMascota(request.POST,instance=per)
        if form.is_valid():
            form.save()
            return redirect('/listamascota')
    data = {'form':form,'titulo':'Modificar Mascota'}
    return render (request,'create.html',data)