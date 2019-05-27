#!/usr/bin/env python
# -*- coding: utf-8 -*-

# lista-productos-autos.py

# Generar e imprimir una lista de productos y autos usando Herencia y
# Polimorfismo de Clases.

# Hacer uso de la metodología MVC

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
        """ Formatea el objeto Producto en str """
        return "{:15} {:>3} {:>10.2f} {:>10.2f}".format(self.nombre,
            self.cantidad, self.precio, self.subtotal)

class Auto(Producto):
    """ Definición del objeto Auto """
    def __init__(self, nombre, cantidad, precio, marca, modelo):
        """ Constructor de la clase Auto """
        super().__init__(nombre, cantidad, precio)
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        """ Formatea el objeto Auto en str """
        return "{:30} {:>3} {:>10.2f} {:>10.2f}".format(
            "{} {} ({})".format(self.marca, self.nombre, self.modelo),
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

def obtener_autos():
    """ Genera una lista de productos de tipo Auto"""
    autos = [
        Auto("Vocho", 3, 20000.00, "WV", 2000),
        Auto("Leon", 1, 185000.00, "Seat", 2020),
        Auto("Camaro", 1, 299000.00, "Chevrolet", 2021)
    ]

    return autos

# Vista
def imprimir_productos(productos, total, margen):
    """
    Imprime la lista productos en la salida estándar en formato
    texto plano.
    """
    for p in productos:
        print(p)
    print(" "*margen + "{:>10.2f}".format(total))

# Controlador
def main():
    """ Función principal del script """
    # Se procesa la lista de productos
    productos = obtener_productos()
    total = sum([p.subtotal for p in productos])
    imprimir_productos(productos, total, 31)

    print()

    # Se procesa la lista de autos 
    autos = obtener_autos()
    total = sum([a.subtotal for a in autos])
    imprimir_productos(autos, total, 46)

if __name__ == "__main__":
    main()
