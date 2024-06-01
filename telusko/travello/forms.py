from django import forms
from .models import Alumno, Curso, NotasAlumnosPorCurso

class IngresarLugar(forms.ModelForm):
  
  class Meta:
    model = Alumno
    fields = ['cui', 'nombre', 'apellidos', 'edad', 'dni']
    
