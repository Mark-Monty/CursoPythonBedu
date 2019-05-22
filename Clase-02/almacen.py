#/usr/bin/env python
# -*- coding: utf-8 -*-

# almacen.py

# Imprime una lista de productos incluyendo
# nombre, cantidad, precio, subtotal y un total
# final utilizando listas.

# Datos
productos = [
    ['Mesa', 100, 3],
    ['Mesa mediana', 200, 2],
    ['Mesa grande', 500, 1]
]

# Calcular el subtotal de cada producto
for p in productos:
    p.append(p[1]*p[2])

# Calcular el total
# total = 0
# for p in productos:
#    total += p[3]  # 3 -> subtotal
total = sum([p[3] for p in productos])

# Imprimir lista de productos
for p in productos:
    print("{:40} {:10} {:5} {:10}".format(*p))
# Imprimir total
print(" "* 58 + "{:10}".format(total))
