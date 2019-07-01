from archivopdf.models import Autor, ArchivoPDF
from rest_framework import serializers

class AutorSerializer(serializers.HyperlinkedModelSerializer):
    """ Representa el modelo Autor en la API """
    class Meta:
        model = Autor
        fields = ('id', 'nombre', 'email', 'sexo', 'registro')
        
class ArchivoPDFSerializer(serializers.HyperlinkedModelSerializer):
    """ Representa el modelo Archivo PDF en la API """
    class Meta:
        model = ArchivoPDF
        fields = ('id', 'nombre', 'archivo', 'fecha', 'tamanio', 'md5sum', 'autor')
        
    
        
