from django.shortcuts import render

# Create your views here.
def display(request):
    return render(request, "index.html")

def displayJuegos(request):
    return render(request, "Juegos.html")

def displayRopa(request):
    return render(request, "Ropa.html")

def displayComida(request):
    return render(request, "Comida.html")