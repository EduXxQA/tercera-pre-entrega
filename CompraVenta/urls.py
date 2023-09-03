from django.urls import path
from CompraVenta.views import auto, stock_autos


urlpatterns = [
    path('actualiza-auto/<marca>/<modelo>/<anio>/', auto),
    path('stock-autos/', stock_autos),
    
]


