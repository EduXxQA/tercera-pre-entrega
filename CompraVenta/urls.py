from django.urls import path
from CompraVenta.views import auto, stock_autos, camioneta, moto


urlpatterns = [
    path('actualiza-auto/<marca>/<modelo>/<anio>/', auto),
    path('actualiza-camioneta/<marca>/<modelo>/<anio>/', camioneta),
    path('actualiza-moto/<marca>/<modelo>/<anio>/', moto),
    path('stock-autos/', stock_autos),
    
]


