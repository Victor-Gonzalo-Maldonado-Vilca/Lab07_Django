from django import forms
from .models import Destination, Delete, Modificar

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['nombreCiudad', 'descripcionCiudad', 'imagenCiudad', 'precioTour', 'ofertaTour']
        
class DeleteForm(forms.ModelForm):
    class Meta:
        model = Delete
        fields = ['nombreCiudad']
        
class ModificarForm(forms.ModelForm):
    class Meta:
        model = Modificar
        fields = ['nombreCiudad']
        
class ModificarFormu(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['nombreCiudad', 'descripcionCiudad', 'imagenCiudad', 'precioTour', 'ofertaTour']
