#!/usr/bin/env python
# -*- coding: utf-8 -*-

# lista-de-personas.py

# Generar e imprimir una lista de personas usando POO

# Metodología MVC

# Definición de objetos o clases
class Persona():
    """ Definición del objeto Persona """
    def __init__(self, nombre, ap_paterno, edad):
        """ Constructor de la clase Persona """
        self.nombre = nombre
        self.ap_paterno = ap_paterno
        self.edad = edad

    @property
    def edad_real(self):
        """ Calcula la edad real """
        return self.edad + 5

    def __str__(self):
        """ formatea el objeot Persona en str """
        return "{:10} {:10} {:>3} {:>3}".format(self.nombre,
            self.ap_paterno, self.edad, self.edad_real)

# Modelo
def obtener_personas():
    """ Genera una lista de personas de tipo Persona """
    # Gerar una lista de instancias del objeto Persona
    personas = [
        Persona("Carlos", "Nateras", 34),
        Persona("Francisco", "Escalante", 30)
    ]

    return personas

# Vista
def imprimir_personas(personas):
    """
    Imprime la lista personas en la salida estándar en formato
    texto plano.
    """
    for p in personas:
        print(p)

# Controlador
def main():
    """ función principal del script """
    personas = obtener_personas()  # Lista de personas con POO
    imprimir_personas(personas)

if __name__ == "__main__":
    main()
