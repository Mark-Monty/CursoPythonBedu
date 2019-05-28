#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Clase-04/agregar-persona.py

# Zona de imports
import sys
import click

# Zona de variables
SALIDA = "personas.csv"

@click.command()
@click.argument("nombre")
@click.argument("edad", type=int)
def agrega_persona(nombre, edad):
    """ Agrega una persona al archivo personas.csv """
    da = open(SALIDA, "a")  # regresa un descriptor de archivo
    da.write("{},{}\n".format(nombre, edad))
    da.close()
    print("Se a agregado el registro {} al archivo {}".format(
        "({}, {})".format(nombre, edad), SALIDA))

### TODO INICIA AQUÍ
if __name__ == "__main__":
    agrega_persona()
