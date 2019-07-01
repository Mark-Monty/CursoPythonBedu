#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, request, static_file

@route('/img/<filename>')
def server_static(filename):
    print(filename)
    return static_file(filename, root='./img/')

@route("/")
def index():
    with open("template/formulario.html", "r") as inhtml:
        html = inhtml.readlines()
        
    return html

@route("/", method="POST")
def index():
    with open("template/formulario_resp.html", "r") as inhtml:
        html = inhtml.read()
    nombre = request.forms.get('nombre')
    sexo = request.forms.get('sexo')
    edad = int(request.forms.get('edad'))
    if sexo == "M":
        edad += 10
    html = html.replace("{nombre}", nombre)
    html = html.replace("{edad}", str(edad))
    
    return html


if __name__ == "__main__":
    # Si es un escript creamos nuestro propio servidor, de lo contrario un servidor externo
    # será el encargado de llamar a la app vía WSGI
    run(host='', port=8000, debug=True, reloader=True)
