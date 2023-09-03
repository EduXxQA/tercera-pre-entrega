from django.urls import path
from CompraVenta.views import *

urlpatterns = [
    path('actualiza-auto/<marca>/<modelo>/<anio>', auto),
    path('stock-autos/', stock_autos),
    
]


