from rest_framework import viewsets
from archivopdf.models import Autor, ArchivoPDF
from archivopdf.serializers import AutorSerializer, ArchivoPDFSerializer


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