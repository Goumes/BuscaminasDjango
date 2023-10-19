from django import forms

class CrearTablero (forms.ModelForm):
    columnas = forms.IntegerField()
    filas = forms.IntegerField()