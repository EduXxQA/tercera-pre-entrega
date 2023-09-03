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
    
def stock_autos(req):
    stock = Auto.objects.all()
    
    return render(req, "stock_autos.html", {"stock_autos": stock})