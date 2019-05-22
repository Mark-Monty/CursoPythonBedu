#!/usr/bin/env python
# -*- coding: utf-8 -*-

# lee-edad.py
# Descripción:
# Lee edad e imprime sólo edades válidas

# Esta es una solución, pero ¿cómo se llega a esta solución?
# ¿es la mejor solución? ¿podrías hacer una más simple?
es_edad = False  # Variable tipo flag (Bandera)
while not num.isdigit(): # True <- not False
    num = input("Escribe una edad: ")
    if num.isdigit() and int(num) > 0:
        es_edad = True

num = int(num)
print("Tu edad es:", num + 3)
