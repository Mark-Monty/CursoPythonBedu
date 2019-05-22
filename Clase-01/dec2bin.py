#!/usr/bin/env python
# -*- coding: utf-8 -*-

# dec2bin.py

# Convertir un valor decimal a binario e imprimir el
# resultado

# Leer datos del usuario
vdec = input("Valor en decimal: ")

# convertir str a int
vdec = int(vdec)

# Convertir el decimal a binario
vbin = bin(vdec)

# Imprimir el resultado
print("Valor en binario:", vbin)
