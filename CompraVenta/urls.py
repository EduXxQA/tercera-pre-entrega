from django.urls import path
from CompraVenta.views import *


urlpatterns = [
    path('actualiza-auto/<marca>/<modelo>/<anio>/', auto),
    path('actualiza-camioneta/<marca>/<modelo>/<anio>/', camioneta),
    path('actualiza-moto/<marca>/<modelo>/<anio>/', moto),
    path('stock-autos/', stock_autos),
    path('stock-camionetas/', stock_camionetas),
    path('stock-motos/', stock_motos),
    path('', inicio),
    path('vista-auto/', vista_auto),
    path('vista-camioneta/', vista_camioneta),
    path('vista-moto/', vista_moto),
    
]


