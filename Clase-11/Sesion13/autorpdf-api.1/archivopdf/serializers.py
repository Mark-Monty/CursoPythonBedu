from archivopdf.models import Autor, ArchivoPDF
from rest_framework import serializers


class ArchivoPDFSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para ArchivoPDF """
    
    class Meta:
        model = ArchivoPDF
        fields = ('id', 'nombre', 'archivo', 'fecha', 'tamanio', 'md5sum', 'autor')


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para Autor"""
    
    archivopdfs = ArchivoPDFSerializer(many=True, read_only=True)
    
    class Meta:
        model = Autor
        fields = ('id', 'nombre', 'email', 'sexo', 'registro', 'archivopdfs')
