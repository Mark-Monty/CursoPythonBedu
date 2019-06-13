#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


with open("img/python-logo.png", "rb") as da:
    imagen = da.read()

# 0 - Entrada estándar
# 1 - Salida estándar
# 2 - Salida de error
os.write(1, b"Content-Type: application/octet-stream\n\n")
os.write(1, imagen)
