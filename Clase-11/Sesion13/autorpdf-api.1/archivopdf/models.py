from django.db import models
# Create your models here.

class Autor(models.Model):
    """ 
        Autor representar a un usuario de tipo Autor y que tienen
        permitido registrar archivos pdf.
    """
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    sexo = models.CharField(max_length=1)
    registro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        """ Define el formato str para la clase Autor """
        return self.nombre

    
class ArchivoPDF(models.Model):
    """ 
        ArchivoPDF representar a un archivo PDF que está relacionado
        con sólo un Autor.
    """
    nombre = models.CharField(max_length=256, null=True, blank=True)
    archivo = models.FileField(max_length=256)
    fecha = models.DateField(auto_now_add=True)
    tamanio = models.PositiveIntegerField(default=0)
    md5sum = models.CharField(max_length=32, null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="archivopdfs")
