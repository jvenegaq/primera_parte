from django.shortcuts import render
from .models import Equipo

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipo/lista_equipos.html', {'equipos': equipos})

