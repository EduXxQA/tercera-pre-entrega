from django.urls import path
from CompraVenta.views import auto, stock_autos, camioneta


urlpatterns = [
    path('actualiza-auto/<marca>/<modelo>/<anio>/', auto),
    path('actualiza-camioneta/<marca>/<modelo>/<anio>/', camioneta),
    path('stock-autos/', stock_autos),
    
]


