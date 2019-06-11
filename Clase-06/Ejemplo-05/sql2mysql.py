#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from modelomysql import ejecuta_sql

def obtiene_sql(archsql):
    """
    Leer las instrucciones SQL desde el archivo ARCHSQL y regresa
    un string con todas las instrucciones
    """
    with open(archsql) as da:
        sql = da.read()

    return sql


@click.command()
@click.argument("archsql", type=click.Path(exists=True))
def sql2mysql(archsql):
    """
    Ejecuta las instrucciones SQL en el archivo ARCHSQL en el servidor
    MariaDB.
    """
    sql = obtiene_sql(archsql)
    if ejecuta_sql(sql):
        print("Los registros se han insertado correctamente!")
    else:
        print("Error al insertar los registros!")

if __name__ == '__main__':
    sql2mysql()
