#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from modelomysql import inserta_registro

@click.command()
@click.argument("nombre")
@click.argument("apellidos")
@click.argument("edad", type=int)
@click.argument("genero")
def agrega_usuario(nombre, apellidos, edad, genero):
    """
    Agrega un registro a la tabla Usuario
    """
    tabla = "Usuario"
    registro = (nombre, apellidos, edad, genero)
    if inserta_registro(tabla, registro):
        print("Se ha inserta el registro correctamente\n")
    else:
        print("Error al insertar el registro")

if __name__ == '__main__':
    agrega_usuario()
