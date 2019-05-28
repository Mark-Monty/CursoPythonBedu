#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Clase-04/agregar-producto.py

# Zona de imports
import sys
import click

# Zona de variables
SALIDA = "productos.csv"

@click.command()
@click.argument("nombre")
@click.argument("cantidad", type=int)
@click.argument("precio", type=float)
def agrega_producto(nombre, cantidad, precio):
    """ Agrega una producto al archivo productos.csv """
    da = open(SALIDA, "a")  # regresa un descriptor de archivo
    da.write("{},{},{}\n".format(nombre, cantidad, precio))
    da.close()
    print("Se a agregado el registro {} al archivo {}".format(
        "({}, {}, {})".format(nombre, cantidad, precio), SALIDA))

### TODO INICIA AQUÍ
if __name__ == "__main__":
    agrega_producto()
