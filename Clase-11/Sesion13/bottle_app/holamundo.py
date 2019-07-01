#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run

@route("/")
def index():
    return "<h1>Hola mundo web usando Bottle!!</h1>"

@route("/hola/<nombre>")
def hola(nombre):
    return "<h2>Hola <span style='color: #ff8800;'>{}</span>, salu2+ desde Bottle!</h2>".format(nombre.upper())


if __name__ == "__main__":
    # Si es un escript creamos nuestro propio servidor, de lo contrario un servidor externo
    # será el encargado de llamar a la app vía WSGI
    run(host='0.0.0.0', port=8000, debug=True, reloader=True)
