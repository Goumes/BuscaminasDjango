from django import forms

class CrearTablero (forms.Form):
    columnas = forms.IntegerField()
    filas = forms.IntegerField()