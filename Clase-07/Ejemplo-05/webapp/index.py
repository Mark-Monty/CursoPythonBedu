#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, static_file

HOST = "localhost"
PORT = 8000

@route('/img/<filename>')
def server_static(filename):
    return static_file(filename, root='img/')

@route("/")
def index():
    with open("formulario.html") as da:
        html = da.readlines()

    return html


if __name__ == "__main__":
    # Inicializa el servidor de la aplicación web
    run(host=HOST, port=PORT, debug=True)
