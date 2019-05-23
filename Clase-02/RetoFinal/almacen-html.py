#/usr/bin/env python
# -*- coding: utf-8 -*-

# almacen-html.py

# Imprime una lista de productos en formato HTML haciendo uso de la etiqueta
# <table></table>.
# - Cada producto deberá ir en una etiqueta <tr></tr>
# - Cada columna o campo deberá ir en una etiqueta <tr>
# - Incluir un renglón con el nombre de las columnas
# - Crear y usar una nueva función llamada imprimir_producto_html()

# Modelo
def obtener_producto():
    """ Obtiene la lista de productos """
    # Datos
    productos = [
        {"nombre":'Mesa', "precio":100, "cantidad":3},
        {"nombre":'Mesa mediana', "precio":200, "cantidad":2},
        {"nombre":'Mesa grande', "precio":500, "cantidad":1}
    ]

    return productos

# Vista
def imprimir_productos(productos, total):
    """ Imprime la lista de productos """
    # Imprimir lista de productos
    for p in productos:
        print("{:40} {:10} {:5} {:10}".format(p["nombre"],
            p["precio"], p["cantidad"], p["subtotal"]))
    # Imprimir total
    print(" "* 58 + "{:10}".format(total))

def imprimir_productos_html(productos, total):
    """ Imprime la lista de productos en formato HTML """
    # Imprime inicio de tabla
    print("<table>")
    # Imprimie encabezado
    print("<tr><th>nombre</th><th>Precio</th><th>Cantidad</th><th>Subtotal</th>")

    # Se define el forma de reglón en formato html
    r = "<tr><td>{}</td><td>{}</td><td>{}</td><td>{:.2f}</td>"

    # Imprimir lista de productos
    for p in productos:
        print(r.format(p["nombre"], p["precio"], p["cantidad"], p["subtotal"]))
    # Imprimir total
    print(r.format("", "", "Total", total))

    # Imprime cierre de tabla
    print("</table>")

# Controler
def main():
    """ Función principal del script (Controlador) """
    productos = obtener_producto()
    # Calcular subtotal de cada producto
    for p in productos:
        p["subtotal"] = p["precio"]*p["cantidad"]
    # Calcular el total
    total = sum([p["subtotal"] for p in productos])
    imprimir_productos_html(productos, total)

# Esto permite a un script funcionar como comando y como módulo
if __name__ == "__main__":
    main()
