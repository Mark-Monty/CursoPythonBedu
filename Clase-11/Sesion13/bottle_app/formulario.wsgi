import os

"""
formulario.wsgi

Este script no permite lanzar una aplicación Bottle/Python por medio del
protoclo WSGI
"""

"""
Nos cambiamos al directorio del script para que rutas relativas y templates
funcionen adecuadamente.
"""
os.chdir(os.path.dirname(__file__))

import bottle

"""
Aquí creamos o importamos nuestra aplicación y no se tiene que usar run()
porque el servidor ahora es externo a nuestro script.
"""

# Se importa el script/módulo de nuestra aplicación
import formulario

# Definimos application como lo pide el estándar WSGI
application = bottle.default_app()
