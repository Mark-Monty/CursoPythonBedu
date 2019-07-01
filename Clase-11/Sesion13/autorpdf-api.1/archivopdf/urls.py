from django.conf.urls import url, include
from rest_framework import routers
from archivopdf import views

router = routers.DefaultRouter()
router.register(r'autores', views.AutorViewSet)
router.register(r'archivopdfs', views.ArchivoPDFViewSet)

# Enlazamos nuestra API usando rutas automáticas
urlpatterns = [
    url(r'^', include(router.urls)),
]