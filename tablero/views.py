from django.shortcuts import render, redirect, get_object_or_404
from .forms import CrearTablero


# Create your views here.

def tablero_create(request):
    if request.method == 'POST':
        form = CrearTablero(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            columnas = cd.get('columnas')
            filas = cd.get('filas')
            return redirect('tablero_show', columnas=columnas, filas=filas)
    else:
        form = CrearTablero()

    return render(request, 'tablero/tablero_create.html', {'form': form})


def index(request):
    return render(request, 'tablero/index.html', {})

def tablero_show(request, columnas, filas):
    return render(request, 'tablero/tablero_show.html', {'columnas': columnas, 'filas': filas})
