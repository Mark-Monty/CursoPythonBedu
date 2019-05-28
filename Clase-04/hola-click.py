#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Clase-04/hola-click.py

# Zona de imports
import click

@click.command()
@click.option("-n", type=int, help="Repite el mensaje N veces")
@click.argument("fulanito")
def hola_click(n, fulanito):
    """ Escribe un mensaje en la salida estánda a FULANITO """
    for i in range(n):
        print("Hola {}!".format(fulanito))

### TODO INICIA AQUÍ
if __name__ == "__main__":
    hola_click()
