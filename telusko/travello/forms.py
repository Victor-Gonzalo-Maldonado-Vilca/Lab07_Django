from django import forms
from .models import Destination, Delete

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['nombreCiudad', 'descripcionCiudad', 'imagenCiudad', 'precioTour', 'ofertaTour']
        
class DeleteForm(forms.ModelForm):
    class Meta:
        model = Delete
        fields = ['nombreCiudad']
