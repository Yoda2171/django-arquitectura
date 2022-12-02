from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('preparacionpabellon/',views.preparacionPabellon,name="preparacionPabellon"),
    path('preparacionpabellon/chequeorecursos/<id>/',views.chequeoRecursos,name="chequeoRecursos"),
    path('preparacionpabellon/chequeorecursos/new/<id>',views.disponibilizarPabellon,name="disponibilizarPabellon"),
    
]
