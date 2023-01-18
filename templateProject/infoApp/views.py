from django.shortcuts import render

# Create your views here.
def displayInfoMarvel(request):
    data = {
        'titulo': 'Marvel',
        'nombre': 'Iron Man',
        'nombreReal': 'Tony Stark',
        'ciudad': 'New York',
        'edad': 43,
        'url': 'https://media.vandalsports.com/i/1706x960/2-2021/20212518520_1.jpg.webp'
    }
    return render(request,'info/info.html',data)

def displayInfoDc(request):
    data = {
        'titulo': 'DC',
        'nombre': 'Superman',
        'nombreReal': 'Clark Kent',
        'ciudad': 'Metrópolis',
        'edad': 43,
        'url': 'https://phantom-elmundo.unidadeditorial.es/fffc80493df258cceb20d6e9ba055b7c/resize/473/f/webp/assets/multimedia/imagenes/2022/08/03/16595421832009.jpg'

    }
    return render(request,'info/info.html',data)