from django.urls import path
from CompraVenta.views import *


urlpatterns = [
    path('actualiza-auto/<marca>/<modelo>/<anio>/', auto),
    path('actualiza-camioneta/<marca>/<modelo>/<anio>/', camioneta),
    path('actualiza-moto/<marca>/<modelo>/<anio>/', moto),
    path('stock-autos/', stock_autos, name="Stock_Autos"),
    path('stock-camionetas/', stock_camionetas, name="Stock_Camionetas"),
    path('stock-motos/', stock_motos, name="Stock_Motos"),
    path('', inicio, name="Inicio"),
    path('vista-auto/', vista_auto, name='Vista_Autos'),
    path('vista-camioneta/', vista_camioneta, name="Vista_Camionetas"),
    path('vista-motos/', vista_moto, name="Vista_Motos"),
    path('agregar-auto/', agregar_auto, name="Agregar_Auto"),
    path('agregar-camioneta/', agregar_camioneta, name="Agregar_Camioneta"),
    path('agregar-moto/', agregar_moto, name="Agregar_Moto"),
    
]


