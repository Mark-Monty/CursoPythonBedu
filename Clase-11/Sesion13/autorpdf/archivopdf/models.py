from django.db import models

# Create your models here.

class Autor(models.Model):
    """ Modelo para manejar un Autor """
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=256)
    sexo = models.CharField(max_length=1)
    registro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        """ Representación en str para Autor """
        return self.nombre
    
class ArchivoPDF(models.Model):
    """ Modelo para manejar un Archivo PDF"""
    nombre = models.CharField(max_length=256, null=True, blank=True)
    archivo = models.FileField(max_length=256)
    fecha = models.DateField(auto_now_add=True)
    tamanio = models.PositiveIntegerField(default=0)
    md5sum = models.CharField(max_length=32, null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)


