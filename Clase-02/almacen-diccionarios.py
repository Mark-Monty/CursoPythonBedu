#/usr/bin/env python
# -*- coding: utf-8 -*-

# almacen.py

# Imprime una lista de productos incluyendo
# nombre, cantidad, precio, subtotal y un total
# final utilizando listas de diccionarios.

# Datos
productos = [
    {"nombre":'Mesa', "precio":100, "cantidad":3},
    {"nombre":'Mesa mediana', "precio":200, "cantidad":2},
    {"nombre":'Mesa grande', "precio":500, "cantidad":1}
]

# Calcular el subtotal de cada producto
for p in productos:
    p["subtotal"] = p["precio"]*p["cantidad"]

# Calcular el total
# total = 0
# for p in productos:
#    total += p[3]  # 3 -> subtotal
total = sum([p["subtotal"] for p in productos])

# Imprimir lista de productos
for p in productos:

    print("{:40} {:10} {:5} {:10}".format(p["nombre"],
        p["precio"], p["cantidad"], p["subtotal"]))
# Imprimir total
print(" "* 58 + "{:10}".format(total))
