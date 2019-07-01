from rest_framework import viewsets
from archivopdf.models import Autor, ArchivoPDF
from archivopdf.serializers import AutorSerializer, ArchivoPDFSerializer
from hashlib import md5


class AutorViewSet(viewsets.ModelViewSet):
    """
    API que permite a los usuario ver o modificar
    """
    queryset = Autor.objects.all().order_by('-registro')
    serializer_class = AutorSerializer


class ArchivoPDFViewSet(viewsets.ModelViewSet):
    """
    API que permite a los usuario ver o modificar
    """
    queryset = ArchivoPDF.objects.all()
    serializer_class = ArchivoPDFSerializer

    def perform_create(self, serializer):
        # Obtenemos el archivo enviado por POST
        arch = self.request.FILES["archivo"]
        # Calculamos el md5
        h = md5(arch.file.read())
        md5sum = h.hexdigest()

        serializer.save(
            nombre=arch.name,
            tamanio=arch.size,
            md5sum=md5sum
        )
        