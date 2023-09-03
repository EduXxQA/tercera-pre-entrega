from django.shortcuts import render
from .models import Auto, Camioneta, Moto
from django.http import HttpResponse

# Create your views here.

def auto(req, marca, modelo, anio):
    auto = Auto(marca = marca, modelo = modelo, anio = anio)
    auto.save()
    
    return HttpResponse(f"""
        <p><strong>Auto:</strong> {auto.marca} - <strong>Modelo:</strong> {auto.modelo} - <strong>Año:</strong> {auto.anio} - <strong>Actualizado!!!</strong></p>                  
    """)
    
def camioneta(req, marca, modelo, anio):
    auto = Camioneta(marca = marca, modelo = modelo, anio = anio)
    auto.save()
    
    return HttpResponse(f"""
        <p><strong>Camioneta:</strong> {auto.marca} - <strong>Modelo:</strong> {auto.modelo} - <strong>Año:</strong> {auto.anio} - <strong>Actualizado!!!</strong></p>                  
    """)    
    
def moto(req, marca, modelo, anio):
    moto = Moto(marca = marca, modelo = modelo, anio = anio)
    moto.save()
    
    return HttpResponse(f"""
        <p><strong>Moto:</strong> {moto.marca} - <strong>Modelo:</strong> {moto.modelo} - <strong>Año:</strong> {moto.anio} - <strong>Actualizado!!!</strong></p>                  
    """) 
    
def stock_autos(req):
     stock = Auto.objects.all()
    
     return render(req, "stock_autos.html", {"stock_autos": stock})
 
def stock_camionetas(req):
     stock = Camioneta.objects.all()
    
     return render(req, "stock_camioneta.html", {"stock_camionetas": stock})
 
def stock_motos(req):
     stock = Moto.objects.all()
    
     return render(req, "stock_motos.html", {"stock_motos": stock})

def inicio(req):
    return HttpResponse("Vista de Inicio")

def vista_auto(req):
    return HttpResponse("Vista de Autos")

def vista_camioneta(req):
    return HttpResponse("Vista de Camionetas")

def vista_moto(req):
    return HttpResponse("Vista de Motos")

