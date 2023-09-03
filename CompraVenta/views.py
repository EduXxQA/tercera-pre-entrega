from django.shortcuts import render
from .models import Auto, Camioneta, Moto
from django.http import HttpResponse, HttpRequest

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
    return render(req, "inicio.html")
    
def vista_auto(req):
    return render(req, "vista_autos.html")
    
def vista_camioneta(req):
    return render(req, "vista_camionetas.html")

def vista_moto(req):
    return render(req, "vista_motos.html")

def agregar_auto(req: HttpRequest):
    
    print('method', req.method)
    print('post', req.POST)
    
    if req.method == 'POST':
        auto = Auto(marca=req.POST["marca"], modelo=req.POST["modelo"], anio=req.POST["anio"])
        auto.save()
        return render(req, "inicio.html", {"mensaje": "Auto agregado con éxito!!"})
        
    return render(req, "agregar_auto.html")    

def agregar_camioneta(req):
    
    print('method', req.method)
    print('post', req.POST)
    
    if req.method == 'POST':
        camioneta = Camioneta(marca=req.POST["marca"], modelo=req.POST["modelo"], anio=req.POST["anio"])
        camioneta.save()
        return render(req, "inicio.html", {"mensaje": "Camioneta agregada con éxito!!"})
    
    return render(req, "agregar_camioneta.html")  

def agregar_moto(req):
    
    print('method', req.method)
    print('post', req.POST)
    
    if req.method == 'POST':
        moto = Moto(marca=req.POST["marca"], modelo=req.POST["modelo"], anio=req.POST["anio"])
        moto.save()
        return render(req, "inicio.html", {"mensaje": "Moto agregada con éxito!!"})
    
    return render(req, "agregar_moto.html")  
