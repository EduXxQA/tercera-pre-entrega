from django.contrib import admin
from .models import * 

class AutoAdmin(admin.ModelAdmin):
    search_fields = ['MARCA']
    
class CamionetaAdmin(admin.ModelAdmin):
    search_fields = ['MARCA']
    
class MotoAdmin(admin.ModelAdmin):
    search_fields = ['MARCA']        
# Register your models here.

admin.site.register(Auto, AutoAdmin)
admin.site.register(Camioneta, CamionetaAdmin)
admin.site.register(Moto, MotoAdmin)
