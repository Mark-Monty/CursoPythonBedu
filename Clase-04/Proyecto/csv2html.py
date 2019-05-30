#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Clase-04/csv2html.py

# Zona de imports
import click
import csv


def obtener_registros(archivo):
    """
    Regresa una lista con todos los registros en archivo, cada registro
    es una lista que contiene cada uno de los campos
    """
    with open(archivo) as da:
        csv_reader = csv.reader(da)
        registros = list(csv_reader)

    return registros

def guarda_html(registros, archivo):
    """ Guarda los registros en el archivo en formato HTML """
    html = """
<html>
<head>
    <title>Lista de {}</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="main.css">
</head>
<body>
    <h1>Lista de {}</h1>
    <table>
        <!-- Lista de renglones -->
        {}
    </table>
</body>
</html>
    """
    renglones = []
    for reg in registros:
        linea = "<tr>"
        for campo in reg: # reg-> Paco, 15
            linea += "<td>{}</td>".format(campo)
            # linea -> "<tr><td>Paco</td>"
            # linea -> "<tr><td>Paco</td><td>15</td>"
        linea += "</tr>"
        # linea -> "<tr><td>Paco</td><td>15</td></tr>"
        renglones.append(linea)
    html = html.format(archivo, archivo, "\n".join(renglones))
    with open(archivo, "w") as da:
        da.write(html)

@click.command()
@click.option("-o", "n", type=int, metavar="N",
    help="Ordena la tabla en base a la columna N")
@click.argument("archivo", type=click.Path(exists=True))
def csv2html(n, archivo):
    """ Agrega una producto al archivo productos.csv """

    # Leer todos los registros del archivo csv
    registros = obtener_registros(archivo)

    # Ordenamos en base la columna n
    if n:
        registros.sort(key=lambda r: r[n-1])

    # Crear el nombre del archivo html
    # archivo.csv -> archivo.html
    archivo_html = archivo.replace(".csv", ".html")

    guarda_html(registros, archivo_html)

### TODO INICIA AQUÍ
if __name__ == "__main__":
    csv2html()
