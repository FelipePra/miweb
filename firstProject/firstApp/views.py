from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def hola(request):
    return  HttpResponse("<h1>Hola vengo de django</h1>")

def semana  (request):
    return HttpResponse("<h1>Nos vemos el fin de semana</h1>")

def hora (request):
    dt = datetime.datetime.now()
    return HttpResponse("<h1>Fecha y Hora:" + str(dt) + "</h1>")

