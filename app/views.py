from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')
    
def login(request):
    return render(request, 'core/login.html')

def preparacionPabellon(request):
    return render(request,'core/preparacion_de_pabellon.html')

def chequeoRecursos(request):
    return render(request,'core/chequeo_recursos.html')