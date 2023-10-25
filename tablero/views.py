from django.shortcuts import render, redirect, get_object_or_404
from .forms import CrearTablero


# Create your views here.

def tablero_create(request):
    if request.method == 'GET' and request.GET:
        form = CrearTablero(request.GET)
        if form.is_valid():
            columnas = request.GET.get('columnas', '')
            filas = request.GET.get('filas', '')
            # return redirect('/tablero_show'+'?columnas='+str(columnas)+'&filas='+str(filas))
            return render(request, 'tablero/tablero_show.html', {'columnas': columnas, 'filas': filas})
    else:
        form = CrearTablero()

    return render(request, 'tablero/tablero_create.html', {'form': form})


def index(request):
    return render(request, 'tablero/index.html', {})

def tablero_show(request):
    columnas = request.GET.get('columnas', '')
    filas = request.GET.get('filas', '')

    return render(request, 'tablero/tablero_show.html', {'columnas': columnas, 'filas': filas})
