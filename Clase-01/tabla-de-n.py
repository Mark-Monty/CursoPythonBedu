#!/usr/bin/env python
# -*- coding: utf-8 -*-

# tabla-del-n.py
n = input("Tabla del n: ")  # regresa un str
n = int(n)  # str -> int

for i in range(1,11):
    r = n * i
    print("{} x {} = {}".format(n, i, r))
