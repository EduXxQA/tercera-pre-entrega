from django.shortcuts import render
from .models import Auto, Camioneta, Moto
from django.http import HttpResponse, HttpRequest
from .forms import *

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
        
        nuevoAuto = AgeragrAuto(req.POST)
        
        if nuevoAuto.is_valid():
            print(nuevoAuto.cleaned_data)
            data = nuevoAuto.cleaned_data
        
            auto = Auto(marca=data["marca"], modelo=data["modelo"], anio=data["anio"])
            auto.save()
            return render(req, "inicio.html", {"mensaje": "Auto agregado con éxito!!"})
        else:
            return render(req, "inicio.html", {"mensaje": "El auto no pudo ser agregado"})            
    else:
        nuevoAuto = AgeragrAuto()
        return render(req, "agregar_auto.html", {"nuevoAuto": nuevoAuto})    

def agregar_camioneta(req: HttpRequest):
    
    print('method', req.method)
    print('post', req.POST)
    
    if req.method == 'POST':
        
        nuevaCamioneta = AgregarCamioneta(req.POST)
        
        if nuevaCamioneta.is_valid():
            print(nuevaCamioneta.cleaned_data)
            data = nuevaCamioneta.cleaned_data
            
            camioneta = Camioneta(marca=data["marca"], modelo=data["modelo"], anio=data["anio"])
            camioneta.save()
            return render(req, "inicio.html", {"mensaje": "Camioneta agregada con éxito!!"})
        else:
            return render(req, "inicio.html", {"mensaje": "La Camioneta no pudo ser agregada"}) 
        
    else:
        nuevaCamioneta = AgregarCamioneta()
        return render(req, "agregar_camioneta.html", {"nuevaCamioneta": nuevaCamioneta})   
    
             
    
      

def agregar_moto(req: HttpRequest):
    
    print('method', req.method)
    print('post', req.POST)
    
    if req.method == 'POST':
        
        nuevaMoto = AgregarMoto(req.POST)
        
        if nuevaMoto.is_valid():
            print(nuevaMoto.cleaned_data)
            data = nuevaMoto.cleaned_data
            
            moto = Moto(marca=data["marca"], modelo=data["modelo"], anio=data["anio"])
            moto.save()
            return render(req, "inicio.html", {"mensaje": "Moto agregada con éxito!!"})
        else:
            return render(req, "inicio.html", {"mensaje": "La moto no pudo ser agregada"}) 
        
    else:
        nuevaMoto = AgregarMoto()
        return render(req, "agregar_moto.html", {"nuevaMoto": nuevaMoto})   
    
    
def busqueda_auto_marca(req):
    return render(req, "busqueda_auto_marca.html") 

def buscarAuto(req):
    
    if req.GET["marca"]:
        marca = req.GET["marca"]
        auto = Auto.objects.get(marca=marca)
        return render(req, "Resultado_busqueda_auto.html", {"autos": auto})  
    else:
        return HttpResponse(f'No escribiste ninguna marca')
        
        
def busqueda_camioneta_marca(req):
    return render(req, "busqueda_camioneta_marca.html") 

def buscarCamioneta(req):
    
    if req.GET["marca"]:
        marca = req.GET["marca"]
        camioneta = Camioneta.objects.get(marca=marca)
        return render(req, "Resultado_busqueda_camioneta.html", {"camioneta": camioneta})  
    else:
        return HttpResponse(f'No escribiste ninguna marca')
    

def busqueda_moto_marca(req):
    return render(req, "busqueda_moto_marca.html") 

def buscarMoto(req):
    
    if req.GET["marca"]:
        marca = req.GET["marca"]
        moto = Moto.objects.get(marca=marca)
        return render(req, "Resultado_busqueda_moto.html", {"moto": moto})  
    else:
        return HttpResponse(f'No escribiste ninguna marca')