#!/usr/bin/env python
# -*- coding: utf-8 -*-

# tabla-de-productos.py
p1 = 6000
p2 = 600
p3 = 60
total = p1 + p2 + p3

# Imprimir en la salida estándar la tabla de productos
print("-"*79)
print("{:40} | {:6}".format("Producto", "Precio"))
print("-"*79)
print("{:40} | {:>10.2f}".format("Laptop Dell", p1))
print("{:40} | {:>10.2f}".format("Mesa", p2))
print("{:40} | {:>10.2f}".format("Multicontacto", p3))
print("-"*79)
print("{:>40} | {:>10.2f}".format("Total", total))
