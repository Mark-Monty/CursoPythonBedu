#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

HOST = "localhost"
PORT = 8000

def hola_mundo_app(environ, start_response):
    """ funcion para atender las peticiones via wsgi """
    status = '200 OK'  # HTTP Status
    headers = [
        ('Content-type', 'text/html; charset=utf-8')
    ]
    start_response(status, headers)

    #if environ["PATH_INFO"] == "/":
        # paginas principal
    #elif environ["PATH_INFO"] == "/contacto":
        # html de contacto

    datos = ["<li><b>{}</b>:{}</li>".format(k, v) for k, v in environ.items()]
    # ["<li>PATH_INFO: valor</li>", ...]
    datos = "\n".join(datos)
    return ["""
   <html>
       <body>
           <h1>Hecho con Python</h1>
           <h3>Hecho con <3</h3>
           <hr />
           <p>Hola {user}!</p>
           <p>
           {datos}
           </p>
       </body>
   </html>
   """.format(user=environ["USER"],datos=datos).encode("utf-8")]

if __name__ == "__main__":
    with make_server(HOST, PORT, hola_mundo_app) as httpd:
        print("Escuchando en {}:{}... [Presiona Cotrol+C para terminar!]".format(HOST, PORT))
        httpd.serve_forever()
