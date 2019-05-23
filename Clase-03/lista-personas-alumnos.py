#!/usr/bin/env python
# -*- coding: utf-8 -*-

# lista-personas-alumnos.py

# Generar e imprimir una lista de personas y de alumnos usando
# una sóla función imprimir_lista()

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

class Alumno(Persona):
    """ Definición del objeto Alumno """
    def __init__(self, nombre, ap_paterno, edad, matricula):
        """ Constructor de la clase Alumno """
        super().__init__(nombre, ap_paterno, edad)
        self.matricula = matricula

    def __str__(self):
        """ formatea el objeto Alumno en str """
        return "{:10} {:10} {:>3} {:>3} {:5}".format(self.nombre,
            self.ap_paterno, self.edad, self.edad_real,
            self.matricula)

# Modelo
def obtener_personas():
    """ Genera una lista de personas de tipo Persona """
    # Gerar una lista de instancias del objeto Persona
    personas = [
        Persona("Carlos", "Nateras", 34),
        Persona("Francisco", "Escalante", 30)
    ]

    return personas

def obtener_alumnos():
    """ Genera una lista de tipo Alumno """
    alumnos = [
        Alumno("Ismael", "Fajardo", 30, "14356"),
        Alumno("Arturo", "Ramírez", 35, "35656"),
    ]

    return alumnos

# Vista
def imprimir_lista(lista):
    """
    Imprime la lista en la salida estándar en formato
    texto plano.
    """
    for i in lista:
        print(i)

# Controlador
def main():
    """ función principal del script """
    # Aplicación de herencia de clases
    personas = obtener_personas()
    alumnos = obtener_alumnos()

    # Aplicación de polimorfismo de clases
    imprimir_lista(personas)
    imprimir_lista(alumnos)

if __name__ == "__main__":
    main()
