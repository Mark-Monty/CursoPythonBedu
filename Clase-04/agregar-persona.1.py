#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Clase-04/agregar-persona.py

# Zona de imports
import sys

# Zona de variables
SALIDA = "personas.csv"

# Controlador
def main(parametros):
    """ Función principal del script """
    da = open(SALIDA, "a")  # regresa un descriptor de archivo
    da.write("{},{}\n".format(*parametros))
    da.close()
    print("Se a agregado el registro {} al archivo {}".format(
        parametros, SALIDA))

### TODO INICIA AQUÍ
if __name__ == "__main__":
    main(sys.argv[1:])
