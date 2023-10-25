from django import forms


class CrearTablero(forms.Form):
    columnas = forms.IntegerField(label='columnas', min_value=1, max_value=15)
    filas = forms.IntegerField(label='filas', min_value=1, max_value=20)
