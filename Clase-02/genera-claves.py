#!/usr/bin/env python
# -*- cofing: utf-8 -*-

# genera-clave.py

import random

# Genera M clave sde longitud N

# Obtención de datos (Modelo)
minicusulas = "abcdefghijklmnopqestuvwxyz"
mayuculas = minicusulas.upper()
digitos = "0123456789"
alfabeto = minicusulas + mayuculas + digitos

# Lectura de datos del usuario
m = input("Cantidad de claves a generar: ")
m = int(m)
n = input("Longitud de clave: ")
n = int(n)

# Genera claves:
claves = []
for i in range(m):
    clave = random.choices(alfabeto, k=n) # Lista
    clave = "".join(clave)  # str
    claves.append(clave)
    print(claves)

# Imprimir lista
for c in claves:
    print(c)
