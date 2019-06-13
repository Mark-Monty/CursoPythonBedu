`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 07`](../Readme.md) > Reto-03

## Conociendo la interface WSGI creando una micro aplicación web con Python.

### OBJETIVO
Aplicar el flujo de información entre un servidor web y una aplicación en Python por medio de la interface WSGI (Web Server Gateway Interface).

#### REQUISITOS
1. Actualizar repositorio

#### DESARROLLO
1. Entendiendo la interface WSGI: Creando la aplicación web en la carpeta `webapp/` con el nombre `imagen.py` de tal forma que pueda responder a las siguientes peticiones:

   - http://localhost:8000/python-logo.png
   - http://localhost:8000/xxx-chicas.png
   - http://localhost:8000/xxx-chicos.png
   - http://localhost:8000/otra.png
   - http://localhost:8000/imagen.py
   - http://localhost:8000/info.py
   ***

#### TIPS
- Hacer uso de módulo `os`
- Hacer uso del módulo `from wsgiref.util import FileWrapper`
- Hacer uso del valor de `environ["PATH_INFO"]`
