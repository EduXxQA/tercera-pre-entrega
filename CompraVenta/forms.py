from django import forms 

class AgeragrAuto(forms.Form):
    marca = forms.CharField(required=True)
    modelo = forms.CharField(required=True)
    anio = forms.IntegerField(required=True)
    
    
class AgregarCamioneta(forms.Form):
    marca = forms.CharField(required=True)
    modelo = forms.CharField(required=True)
    anio = forms.IntegerField(required=True)

class AgregarMoto(forms.Form):
    marca = forms.CharField(required=True)
    modelo = forms.CharField(required=True)
    anio = forms.IntegerField(required=True)

