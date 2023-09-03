from django.db import models

# Create your models here.

class Auto(models.Model):
    
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField(max_length=4)
    
class Camioneta(models.Model):

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField(max_length=4)
    
class Moto(models.Model):
   
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField(max_length=4)
    