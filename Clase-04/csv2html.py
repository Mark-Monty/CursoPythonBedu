#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Clase-04/csv2html.py

# Zona de imports
import click
import csv

def guarda_html(registros, archivo):
    """ Guarda los registros en el archivo en formato HTML """
    html = """
<html>
<head>
   <title>Lista de personas</title>
</head>
<body>
    <h1>Lista de personas</h1>
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
    html = html.format("\n".join(renglones))
    with open(archivo, "w") as da:
        da.write(html)

@click.command()
@click.argument("archivo", type=click.Path(exists=True))
def csv2html(archivo):
    """ Agrega una producto al archivo productos.csv """
    # Leer todos los registros del archivo csv
    with open(archivo) as da:
        csv_reader = csv.reader(da)
        registros = list(csv_reader)

    # Crear el nombre del archivo html
    # archivo.csv -> archivo.html
    archivo_html = archivo.replace(".csv", ".html")

    guarda_html(registros, archivo_html)

### TODO INICIA AQUÍ
if __name__ == "__main__":
    csv2html()
