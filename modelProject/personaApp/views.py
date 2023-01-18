from tkinter.tix import Form
from django.shortcuts import redirect, render
from django.contrib import messages
from personaApp.forms import FormPersona
from personaApp.models import Persona 

# Create your views here.

def createpersona (request):
    form = FormPersona()
    if request.method == 'POST':
        form = FormPersona(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Persona agregada con exito!!!')
            return listapersona(request)    
    data = {'form':form,'titulo':'Crear Persona'}
    return render(request, 'create.html',data)

def listapersona (request):
    lista = Persona.objects.all()
    data = {'personas' : lista}
    return render(request, 'Index.html',data)

#metodo para eliminar
def eliminarpersona(request,id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('/lista')

def editarpersona(request,id):
    per = Persona.objects.get(id=id)
    form = FormPersona(instance=per)
    if request.method == 'POST':
        form = FormPersona(request.POST,instance=per)
        if form.is_valid():
            form.save()
            return redirect('/lista')
    data = {'form':form,'titulo':'Modificar Persona'}
    return render (request,'create.html',data)