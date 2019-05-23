#!/usr/bin/env python
# -*- coding: utf-8 -*-

# lista-de-productos.py

# Generar e imprimir una lista de productos usando POO

# Metodología MVC

# Definición de objetos o clases
class Producto():
    """ Definición del objeto Producto """
    def __init__(self, nombre, cantidad, precio):
        """ Constructor de la clase Producto """
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    @property
    def subtotal(self):
        """ Calcula el subtotal """
        return self.precio * self.cantidad

    def __str__(self):
        """ formatea el objeto Producto en str """
        return "{:15} {:>3} {:>10.2f} {:>10.2f}".format(self.nombre,
            self.cantidad, self.precio, self.subtotal)

# Modelo
def obtener_productos():
    """ Genera una lista de productos de tipo Producto """
    # Gerar una lista de instancias del objeto Producto
    productos = [
        Producto("Mesa chica", 5, 100.00),
        Producto("Mesa mediana", 3, 185.00),
        Producto("Mesa grande", 1, 299.00)
    ]

    return productos

# Vista
def imprimir_productos(productos, total):
    """
    Imprime la lista productos en la salida estándar en formato
    texto plano.
    """
    for p in productos:
        print(p)
    print(" "*31 + "{:>10.2f}".format(total))

# Controlador
def main():
    """ función principal del script """
    productos = obtener_productos()  # Lista de productos con POO
    total = sum([p.subtotal for p in productos])
    imprimir_productos(productos, total)

if __name__ == "__main__":
    main()
