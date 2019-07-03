from rest_framework import serializers

from .models import Usuario, Libro, Prestamo

class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
  """ Serializador para atender las conversiones para Prestamo """
  class Meta:
      # Se define sobre que modelo actua
      model = Prestamo
      # Se definen los campos a incluir
      fields = ('id', 'usuario', 'fechaPre', 'fechaDev')


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Usuario """
    # Vincular la tabla Usuario con la tabla Prestamo
    prestamos = PrestamoSerializer(many=True, read_only=True)
    class Meta:
        # Se define sobre que modelo actua
        model = Usuario
        # Se definen los campos a incluir
        fields = ('id', 'nombre', 'apellidos', 'edad', 'genero', 'direccion', 'prestamos')


class LibroSerializer(serializers.HyperlinkedModelSerializer):
   """ Serializador para atender las conversiones para Libro """
   class Meta:
       # Se define sobre que modelo actua
       model = Libro
       # Se definen los campos a incluir
       fields = ('id', 'titulo', 'editorial', 'numPag', 'autores')
