from django.db import models

class Infraestructura(models.Model):
    id_infraestructura = models.BigAutoField(primary_key=True,verbose_name="Id Infraestructura")
    nombre= models.CharField(max_length=50,verbose_name="Nombre Infraestructura")
    estado=models.CharField(max_length=50,verbose_name="Estado")
    
    def serializer(self):
        return {
            "id_infraestructura":self.id_infraestructura,
            "nombre":self.nombre,
            "estado":self.estado
        }

class RecursoHumano(models.Model):
    id_recursohumano= models.BigAutoField(primary_key=True,verbose_name="Id Recurso Humano")
    estado = models.CharField(max_length=50,verbose_name="Estado")

    def __str__(self):
        return self.estado

class InsumoEspecifico(models.Model):
    id_insumoEspecifico = models.BigAutoField(primary_key=True,verbose_name="Id insumo Espesifico")
    nombre = models.CharField(max_length=50,verbose_name="Nombre Insumo Especifico")
    estado = models.CharField(max_length=50,verbose_name="Estado")

    def serializer(self):
        return {
            "id_insumoEspecifico":self.id_insumoEspecifico,
            "nombre":self.nombre,
            "estado":self.estado
        }
        

class Cirugia(models.Model):
    id_cirugia = models.BigAutoField(primary_key=True,verbose_name="Id Cirugia")
    tipo= models.CharField(max_length=50,verbose_name="Tipo de Cirugia")

    def __str__(self):
        return self.tipo

class Doctor(models.Model):
    id_doctor = models.BigAutoField(primary_key=True,verbose_name="Id doctor")
    nombre = models.CharField(max_length=50,verbose_name="Nombre Doctor")

    def __str__(self):
        return self.nombre
    

class Pabellon(models.Model):
    id_pabellon = models.BigAutoField(primary_key=True)
    nombrePabellon= models.CharField(max_length=50,verbose_name="Nombre Pabellon")
    disponible = models.CharField(max_length=50,verbose_name="disponible",default="Preparacion")
    id_doctor = models.ForeignKey(Doctor, models.CASCADE,db_column='id_doctor',verbose_name='Doctor') 
    id_cirugia = models.ForeignKey(Cirugia,models.CASCADE,db_column='id_cirugia',verbose_name='Cirugia')
    id_recursohumano=models.ForeignKey(RecursoHumano,models.CASCADE,db_column='id_recursohumano',verbose_name='Recurso Humano')
    id_insumoEspecifico=models.ManyToManyField(InsumoEspecifico,db_column='id_insumoEspecifico',verbose_name='insumo Especifico')
    id_infraestructura=models.ManyToManyField(Infraestructura,db_column='id_infraestructura',verbose_name='Infraestructura')


    def serializer(self):
        return{
            "id_pabellon":self.id_pabellon,
            "nombrePabellon":self.nombrePabellon,
            "disponible":self.disponible,
            "id_doctor":self.id_doctor,
            "id_cirugia":self.id_cirugia,
            "id_insumoEspecifico":self.id_insumoEspecifico,
            "id_recursohumano":self.id_recursohumano,
            "id_infraestructura":self.id_infraestructura
       }

