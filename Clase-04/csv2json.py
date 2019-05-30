#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Clase-04/csv2json.py

# Zona de imports
import click
import csv
import json

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

def guarda_json(registros, archivo):
    """ Guarda los registros en formato json en archivo """
    # Generar lista de diccionarios
    lista = []
    for r in registros:
        lista.append(
            {
                "nombre":r[0],
                "cantidad":r[1],
                "precio":r[2]
            }
        )

    # Crear archivo json
    with open(archivo, "w") as da:
        json.dump(lista, da, indent=4)

@click.command()
@click.argument("archivo", type=click.Path(exists=True))
def csv2json(archivo):
    """ Convierte el archivo productos.csv a productos.json """
    # Leer todos los registros del archivo csv
    with open(archivo) as da:
        csv_reader = csv.reader(da)
        registros = list(csv_reader)

    # Crear el nombre del archivo json
    # archivo.csv -> archivo.json
    archivo_json = archivo.replace(".csv", ".json")

    guarda_json(registros, archivo_json)

### TODO INICIA AQUÍ
if __name__ == "__main__":
    csv2json()
