from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tablero_create', views.tablero_create, name='tablero_create'),
]