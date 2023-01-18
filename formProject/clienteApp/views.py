from django.shortcuts import render

# Create your views here.

def Cliente(request):
    data = {
        'Run': '',
        'Nombre': '',
        'Direccion': '',
        'Email': '',
        'Fono': ''
    }
    return render (request,'')


    