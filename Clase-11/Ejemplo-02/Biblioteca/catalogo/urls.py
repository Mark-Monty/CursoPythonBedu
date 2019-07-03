from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework import routers
from . import views

# Inicializa la ruta para Django Rest
router = routers.DefaultRouter()
# Agregamos rutas para el API /api/
router.register(r'usuarios', views.UsuarioViewSet)  # /api/usuarios
router.register(r'libros', views.LibroViewSet)  # /api/libros

urlpatterns = [
    path("", views.index, name="index"),
    path("prestamo/nuevo/", views.nuevo_prestamo, name="nuevo_prestamo"),
    path("prestamo/<int:idPrestamo>/libros/elimina/<int:idLibro>/",
        views.elimina_libros_prestamo, name="elimina_libros_prestamo"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    # Rutas para el API api/
    path("api/", include(router.urls)),
    # Rutas para la autenticación url /api/auth/
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
]
