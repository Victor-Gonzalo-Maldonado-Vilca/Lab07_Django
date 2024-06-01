from django.db import models

# Create your models here.

class Destination(models.Model):
    nombreCiudad = models.CharField(max_length=100)
    descripcionCiudad = models.TextField()
    imagenCiudad = models.ImageField(upload_to='images/', default='default_image.jpg')
    precioTour = models.DecimalField(max_digits=10, decimal_places=2)
    ofertaTour = models.BooleanField(default=False)

    def __str__(self):
        return self.nombreCiudad

class Delete(models.Model):
    nombreCiudad = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombreCiudad
      
class Modificar(models.Model):
    nombreCiudad = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombreCiudad