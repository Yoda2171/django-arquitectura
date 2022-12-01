from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('preparacionpabellon/',views.preparacionPabellon,name="preparacionPabellon"),
    path('preparacionpabellon/chequeorecursos',views.chequeoRecursos,name="chequeoRecursos"),
    path('login/', views.login),
]
