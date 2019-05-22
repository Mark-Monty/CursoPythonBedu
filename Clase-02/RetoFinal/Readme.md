## RETO FINAL

### DESCRIPCIÓN

Modificar el script `almacen-funciones.py` para que imprima la lista de productos en formato HTML.

### SUGERENCIAS

Usar la función `imprimir_productos()` como base para crear la función `imprimir_productos_html()`, esta función tiene que hacer uso de instrucciones `print()` para ir armando le código HTML final.

Por ejemplo para imprimir la línea con la etiqueta `<table>` sería:

    print("<table>")

### Resultado

Se espera contar con un script llamado `almacen-html.py` que al ser ejecutado
muestre el resultado siguiente:

```
Clase-02 $ python almacen-html.py
<table>
<tr><th>Nombre</th><th>Precio</th><th>Cantidad</th><th>Subtotal</th>
<tr><td>Mesa</td><td>100</td><td>3</td><td>300.00</td>
<tr><td>Mesa mediana</td><td>200</td><td>2</td><td>400.00</td>
<tr><td>Mesa grande</td><td>500</td><td>1</td><td>500.00</td>
<tr><td></td><td></td><td></td><td>1200.00</td>
</table>

Clase-02 $ 
```
