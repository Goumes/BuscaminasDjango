from django.shortcuts import render
from .forms import CrearTablero

# Create your views here.

def tablero_create (request):
    form = CrearTablero()
    if request.method == 'POST':
        form = CrearTablero(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # now in the object cd, you have the form as a dictionary.
            columnas = cd.get('columas')
            filas = cd.get('filas')


    return render (request, 'tablero/tablero_create.html', {'form': form})

def index (request):
    return render (request, 'tablero/index.html', {})