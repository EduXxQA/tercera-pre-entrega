from django.db import models

# Create your models here.

class Auto(models.Model):
    
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    
    def __str__(self):
        return f'{self.marca} - {self.modelo} - {self.anio}'
    
    
class Camioneta(models.Model):

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    
    def __str__(self):
        return f'{self.marca} - {self.modelo} - {self.anio}'
    
class Moto(models.Model):
   
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    
    def __str__(self):
        return f'{self.marca} - {self.modelo} - {self.anio}'
    