
# Creando una API para administrar documentos PDF y autores con Django más DjangoRest

## Preparando nuestro ambiente virtual de trabajo

En Python hay varias maneras de crear ambientes virtuales de trabajo (virtualenv), que son espacios de trabajo aislados de la instalación principal del sistema operativo y que permiten realizar configuraciones e instalaciones para una aplicación en particular sin interferir con lo ya instalado en el sistema o lo instalado por otros proyectos.

Lo primero es crear el ambiente virtual para nuestro proyecto que llamaremos **`AutorPDF_API`**:

```bash
Sesion13 $ conda create -n autorpdf_api python=3.6
Solving environment: done

## Package Plan ##

  environment location: /home/rctorr/miniconda3/envs/autorpdf_api

  added / updated specs:
    - python=3.6


The following NEW packages will be INSTALLED:

    ca-certificates: 2018.03.07-0
    certifi:         2018.8.24-py36_1
    libedit:         3.1.20170329-h6b74fdf_2
    libffi:          3.2.1-hd88cf55_4
    libgcc-ng:       8.2.0-hdf63c60_1
    libstdcxx-ng:    8.2.0-hdf63c60_1
    ncurses:         6.1-hf484d3e_0
    openssl:         1.0.2p-h14c3975_0
    pip:             10.0.1-py36_0
    python:          3.6.6-hc3d631a_0
    readline:        7.0-h7b6447c_5
    setuptools:      40.2.0-py36_0
    sqlite:          3.24.0-h84994c4_0
    tk:              8.6.8-hbc83047_0
    wheel:           0.31.1-py36_0
    xz:              5.2.4-h14c3975_4
    zlib:            1.2.11-ha838bed_2

Proceed ([y]/n)? y
...
Sesion13 $ 
```

Lo siguiente es activar el ambiente con:

```bash
Sesion13 $ source activate autopdf_api
(autorpdf_api) Sesion13 $ 
```

## Instalando nuestras herramientas de desarrollo

Para realizar está API vamos a hacer uso de dos herramientas disponibles para Python:
1. **Django** que es un poderoso, flexible, completo, seguro y para desarrollo ágil de aplicaciones web, el sitio principal es https://www.djangoproject.com
1. **Django-Rest-Framework** es un módulo construido por encima de Django que simplifica la creación de un API con todos los requerimientos que una API requiere, el sitio principal es http://www.django-rest-framework.org

Se instala el Django con pip de la siguiente forma:

```bash
(autorpdf_api) Sesion13 $ pip install django==1.11
Collecting django==1.11
  Downloading https://files.pythonhosted.org/packages/47/a6/078ebcbd49b19e22fd560a
2348cfc5cec9e5dcfe3c4fad8e64c9865135bb/Django-1.11-py2.py3-none-any.whl (6.9MB)
    100% |████████████████████████████████| 6.9MB 429kB/s
Collecting pytz (from django==1.11)
  Using cached https://files.pythonhosted.org/packages/30/4e/27c34b62430286c6d5917
7a0842ed90dc789ce5d1ed740887653b898779a/pytz-2018.5-py2.py3-none-any.whl
Installing collected packages: pytz, django
Successfully installed django-1.11 pytz-2018.5
(autorpdf_api) Sesion13 $ 
```

Se instala el Django-Rest-Framework con pip de la siguiente forma:

```console
(autorpdf_api) Sesion13 $ pip install djangorestframework
Collecting djangorestframework
  Using cached https://files.pythonhosted.org/packages/90/30/ad1148098ff0c375df2a3
0cc4494ed953cf7551fc1ecec30fc951c712d20/djangorestframework-3.8.2-py2.py3-none-any
.whl
Installing collected packages: djangorestframework
Successfully installed djangorestframework-3.8.2
(autorpdf_api) Sesion13 $ 
```

## Descripción de nuestra API

Nuestra API se llamará `AutorPDF_API` y nos permitirá administrar, el registro, consulta, modificación y eliminación de Autores y Archivos PDF, además existe una relación de uno a muchos entre Autor y ArchivoPDF, es decir, cada autor puede tener uno o más archivos pdf registrados, mientras que un ArchivoPDF sólo puede estar asociado a un Autor.

El modelo de clases propuesto sería:

| Autor |
---
| id |
| nombre |
| email |
| sexo |
| fecha_registro |

| ArchivoPDF |
---
| id |
| nombre |
| archivo |
| fecha |
| tamanio |
| md5sum |
| autor |


## Creando nuestro proyecto en Django y nuestra primer aplicación

El proyecto se crea con el comando:

```bash
(autorpdf_api) Sesion13 $ django-admin startproject autorpdf
(autorpdf_api) Sesion13 $ cd autorpdf
(autorpdf_api) Sesion13 $ 
```

Ahora creamos una aplicación que es donde recidirá toda la lógica

```bash
(autorpdf_api) Sesion13/autorpdf $ django-admin startapp archivopdf
(autorpdf_api) Sesion13/autorpdf $ tree
tree
.
├── archivopdf
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── autorpdf
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

3 directories, 12 files
(autorpdf_api) Sesion13/autorpdf $
```

## Inicializando la BD del proyecto

Django ya cuenta con un mecanismo para administrar la BD y configurar elementos de inicio que toda app debe contener, así que realizamos esta inicialización con el comando:

```bash
(autorpdf_api) Sesion13/autorpdf $ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK
(autorpdf_api) Sesion13/autorpdf $
```

## Se crea el usuario administrador del proyecto

Debido a que una app necesita usuarios, Django sabe de usuarios, por lo que es necesario contar con un usuario administrador y que creamos con:

```bash
(autorpdf_api) Sesion13/autorpdf $ python manage.py createsuperuser
Username (leave blank to use 'rctorr'): admin
Email address: admin@ejemplo.com
Password:
Password (again):
Superuser created successfully. 
(autorpdf_api) Sesion13/autorpdf $
```

Lo anterio ha creado el usuario **admin** con email admin@ejemplo.com y clave **password1234**.

## Se ejecuta el proyecto y se verifica su funcionalidad

A este punto ya tenemos un proyecto funcional y para verificarlo se ejecuta la siguiente instrucción:

```bash
(autorpdf_api) Sesion13/autorpdf $ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
September 17, 2018 - 04:25:02Django version 1.11, using settings 'autorpdf.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[17/Sep/2018 04:25:08] "GET / HTTP/1.1" 200 1716
```

El mensaje anterior nos indica que la aplicación ya se está ejecutando y que se puede acceder desde el navegador en la url:
- http://127.0.0.1:8000

Lo que deberá de mostrar algo similar a:

![Captura de primer ejecución de proyecto Django](django-0.png)


## Se crean los modelos usando el ORM de Django

Agregamos nuestros modelos al archivo `archivopdf/models.py`, primero agregamos el modelo para Autor:

```python
class Autor(models.Model):
    """ 
        Autor representar a un usuario de tipo Autor y que tienen
        permitido registrar archivos pdf.
    """
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    sexo = models.CharField(max_length=1)
    registro = models.DateField(auto_now_add=True)
```



Agregamos el modelo para ArchivoPDF:

```python
class ArchivoPDF(models.Model):
    """ 
        ArchivoPDF representar a un archivo PDF que está relacionado
        con sólo un Autor.
    """
    nombre = models.CharField(max_length=256)
    archivo = models.FileField(max_length=256)
    fecha = models.DateField(auto_now_add=True)
    tamanio = models.PositiveIntegerField(default=0)
    md5sum = models.CharField(max_length=32)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="archivopdfs")
```

Ahora le decimos al proyecto en Django que existe una app llamada `archivopdf`  modificando el archivo `autorpdf/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'archivopdf',
]
```

Ahora le decimos a Django que hay nuevos modelos y que tiene que prepararse para agregarlos a la BD, esto lo realizamos con:

```bash
(autorpdf_api) Sesion13/autorpdf $ python manage.py makemigrations
Migrations for 'archivopdf':
  archivopdf/migrations/0001_initial.py
    - Create model ArchivoPDF
    - Create model Autor
    - Add field autor to archivopdf
(autorpdf_api) Sesion13/autorpdf $ 
```

Y finalmente actualizamos la estructura de la BD:

```bash
(autorpdf_api) Sesion13/autorpdf $ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, archivopdf, auth, contenttypes, sessions
Running migrations:
  Applying archivopdf.0001_initial... OK

(autorpdf_api) Sesion13/autorpdf $ 
```

## Se crean los serializadores que pide Django Rest Framework

Creamos el archivo `archivopdf/serializers.py` con el siguiente contenido:

```python
from archivopdf.models import Autor, ArchivoPDF
from rest_framework import serializers


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ('nombre', 'email', 'sexo', 'registro', 'archivopdfs')


class ArchivoPDFSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArchivoPDF
        fields = ('nombre', 'archivo', 'fecha', 'tamanio', 'md5sum', 'autor')
```

## Se crean las vistas

Las vistas son las encargadas de generar resultados en html, json, etc.

Abrimos el archivo `archivopdf/views.py` y lo remplazamos por el siguiente contenido:

```python
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
```

## Se crean las rutas o ¡urls! para la aplicación `archivopdf`

Tomando como base las aplicaciones creadas con Bottle, en Django también es necesario definir las rutas, esto se hará en el archivo `archivopdf/urls.py` agregando el siguiente contenido:

```python
from django.conf.urls import url, include
from rest_framework import routers
import archivopdf.views

router = routers.DefaultRouter()
router.register(r'autores', views.AutorViewSet)
router.register(r'archivopdfs', views.ArchivoPDFViewSet)

# Enlazamos nuestra API usando rutas automáticas
urlpatterns = [
    url(r'^', include(router.urls)),
]
```

## Se crean las rutas para el proyecto

En en caso de Django existen dos lugares de definición de rutas, uno es donde se definen las rutas del proyecto completo y que bien podrían crearse todas las rutas necesarias, es mejor segementar las rutas por aplicación y que ya se crearon con el archivo anterior, ahora corresponde integrarlas a las rutas del proyecto, para ello modificamos el archivo
`autorpdf/urls.py`:

```python
from django.conf.urls import url, include
from django.contrib import admin

from archivopdf import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(urls)),
    # Adicionalmente, también incluimos las URL para hacer login
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
```

## Agregando Django Rest Framework al proyecto de Django

Ahora le decimos al proyecto en Django que existe una app llamada `rest_framework`  modificando el archivo `autorpdf/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'archivopdf',
    'rest_framework',
]
```

## Se ejecuta el nuevamente proyecto

A este punto ya deberíamos de tener nuestra API funcionando, lo ejecutamos con:

```bash
(autorpdf_api) Sesion13/autorpdf $ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
September 17, 2018 - 04:25:02Django version 1.11, using settings 'autorpdf.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[17/Sep/2018 04:25:08] "GET / HTTP/1.1" 200 1716
```

Acceder desde el navegador en la url:
- http://127.0.0.1:8000

Lo que deberá de mostrar algo similar a:

![Captura de primer ejecución de API](django-1.png)


## Corrigiendo error de la url /api/autores/

Al abrir la url mencionada se observa el siguiente error en la terminal donde está corriendo el servidor:

```bash
  File "/home/rctorr/miniconda3/envs/autorpdf_api/lib/python3.6/site-packages/rest_framework/serializers.py", line 1302, in build_unknown_field
    (field_name, model_class.__name__)
django.core.exceptions.ImproperlyConfigured: Field name `archivopdfs` is not valid for model `Autor`.
[17/Sep/2018 06:22:14] "GET /api/autores/ HTTP/1.1" 500 126991
```

Esto es debido a que el campo `archivopdfs` en el modelo de Autor no existe, pero se ha incluido para que dado un autor se pueda ver la lista de archivos pdfs registrados por ese autor, pero para que funcione hay que modificar el archivo `serializers.py` de la siguiente forma:

```python
class ArchivoPDFSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para ArchivoPDF """
    
    class Meta:
        model = ArchivoPDF
        fields = ('nombre', 'archivo', 'fecha', 'tamanio', 'md5sum', 'autor')


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para Autor"""
    
    archivopdfs = ArchivoPDFSerializer(many=True, read_only=True)
    
    class Meta:
        model = Autor
        fields = ('nombre', 'email', 'sexo', 'registro', 'archivopdfs')
```

Guardar los cambios y entrar nuevamente a la url:
- http://localhost:8000/api/autores/

Notar que no es necesario reiniciar el servidor, en automático Django detecta si se ha modificado algún archivo y reinicia el servidor.

Y se puede observar que no hay autores registrados, pero Django REST Framework nos crea todo lo necesario para consultar o agregar elementos a nuestra lista de autores o de archivos, así que agregaremos unos autores primero.

## Corregir problemas al agregar archivos pdf

Lo primero, es que al agregar un archivo se muestra la lista de los autores diponibles, pero se muestra el nombre de la forma **Autor Object**, esto es así, porque en los modelos no se ha agregado el método `__str__()`, así que hay que agregarlo y actualizar la página.


Ahora si ya se puede seleccionar el autor, se agrega un archivo, se le da un nombre y al momento de agregar el archivo nos indica que el md5sum es necesario y eso es así porque en el modelo para el atributo no definimos un valor por default.

Para resolver el problema anterior lo que vamos a hacer es sobre escribir el método `perform_create()` en la vista `ArchivoPDFViewSet()` en el archivo `archivopdf/views.py`:

```python
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
```

Con lo anterior ya podemos adjuntar un archivo y agregarlo a la base de datos, pero los archivos se almacenan en el directorio principal de la aplicación y desde ahí no podremos accederlos, parea resolver esto, realizamos lo siguiente:

1. Creamos la carpeta `Sesion13/autorpdf/media`
1. En el archivo `Sesion13/autorpdf/autopdf/settings.py` se agregan las siguientes líneas al final del archivo:
```python
# Esto es para definir en donde se guardan los archivos
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```
3. En el archivo `Sesion13/autorpdf/autopdf/urls.py` se agregan los siguientes módulos y líneas al final del archivo:

```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Ahora hay que eliminar los registros de arcvhios creados y agregar uno nuevo y luego acceder al archivo pdf desde la API

## Accediendo al API desde una página web por medio de AJAX usando AngularJS

Para acceder a la API se puede realizar desde la misma aplicación web creada en Django o desde cualquier otra aplicación externa, en este caso se usará un archivo html que hace uso de AJAX por medio de AngularJS para acceder a las respuestas del API.

Para que lo anterior sea posible, hay que modificar la aplicación para permitir llamadas remotas a la API desde una aplicación que está fuerá de la aplicación en Django por lo cual agregamos el archivo `cors.py` a la carpeta `archivopdf/cors.py`.

El anterior script contiene una clase que permite a aplicaciones remotas acceder a la información, sin mebargo esto es sólo ejemplificativo ya que podría generar un hueco de seguridad se recomienda hacer uso de credenciales de acceso.

Finalmente en el archivo `autorpdf/settings.py` en la sección de Middlewares se agrega la línea:

```python
    'archivopdf.cors.CorsMiddleware',
```

Una vez realizado lo anterior, abrir el archivo `autorpdf-web/index.html`


```python
from IPython.display import IFrame
IFrame("autorpdf-web/index.html", 500, 450)
```





        <iframe
            width="500"
            height="450"
            src="autorpdf-web/index.html"
            frameborder="0"
            allowfullscreen
        ></iframe>
        




```python

```
