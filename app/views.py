from django.shortcuts import render, redirect
from app.models import Pabellon, Infraestructura,InsumoEspecifico
from django.contrib.auth.decorators import  login_required


# Create your views here.




def index(request):
  
    return render(request, 'core/login.html')    

@login_required
def preparacionPabellon(request):
    pabellon = Pabellon.objects.all();
    pabellon= list(map(lambda pabellon: pabellon.serializer(), pabellon))
    
    return render(request,'core/preparacion_de_pabellon.html',{"pabellones":pabellon})


@login_required
def chequeoRecursos(request , id):
    pabellon = Pabellon.objects.all();
    pabellon= list(map(lambda pabellon: pabellon.serializer(), pabellon))

    infraestructura= Pabellon.objects.get(id_pabellon=id).id_infraestructura.all()
    infraestructura=list(map(lambda infraestructura: infraestructura.serializer(), infraestructura))

    insumo =Pabellon.objects.get(id_pabellon=id).id_insumoEspecifico.all()
    insumo =list(map(lambda insumo: insumo.serializer(), insumo))
    
    rrhh=Pabellon.objects.get(id_pabellon=id).id_recursohumano
    disponibilidad =Pabellon.objects.get(id_pabellon=id).disponible
   
    id_pabellon = Pabellon.objects.get(id_pabellon=id).id_pabellon

    malInsumo = Pabellon.objects.get(id_pabellon=id).id_insumoEspecifico.filter(estado='Malas')
    malInsumo =list(map(lambda insumo: insumo.serializer(), malInsumo))

    malInfraestructura= Pabellon.objects.get(id_pabellon=id).id_infraestructura.filter(estado='Malas')
    malInfraestructura= list(map(lambda infraestructura: infraestructura.serializer(), malInfraestructura))

    malRecursoHumano =  Pabellon.objects.get(id_pabellon=id).id_recursohumano

    print(malRecursoHumano)
    if(len(malInfraestructura) != 0 or len(malInfraestructura) !=0 or malRecursoHumano =="No asignado"):
        return render(request,'core/chequeo_recursos.html',{"malRecursoHumano":malRecursoHumano,"malInsumo":malInsumo,"malInfraestructura":malInfraestructura,"insumo":insumo,"pabellon":pabellon,"infraestructura":infraestructura,"rrhh":rrhh,"disponibilidad":disponibilidad,"id_pabellon":id_pabellon})
    else:
        return render(request,'core/chequeo_recursos.html',{"insumo":insumo,"pabellon":pabellon,"infraestructura":infraestructura,"rrhh":rrhh,"disponibilidad":disponibilidad,"id_pabellon":id_pabellon})

    

@login_required
def disponibilizarPabellon(request,id):
    pabellon = Pabellon.objects.get(id_pabellon=id)
    pabellon.disponible = "Disponible!"
    pabellon.save()
    print(pabellon)
    return redirect('preparacionPabellon')