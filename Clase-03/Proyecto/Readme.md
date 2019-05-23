## Proyecto de clase

### DESCRIPCIÓN

Copiar el script `lista-productos.py` en el script `lista-productos-autos.py`

Modificar el script `lista-productos-autos.py` para que:
1. Imprima la lista de 3 Productos incluyendo el total
1. Imprimir la lista de 3 Autos incluyendo el total
1. Crear la clase `Auto` haciendo uso del concepto de Herencia.
1. Aplicar el concepto de Polimorfismo en ambas clases para poder usar la función `imprime_productos()`
   para imprimir tanto Productos como Autos.

### Diagrama de clases

Se muestra a continuación el diagrama de clases donde se muestra el nombre, los atributos,
los métodos y la relación de herencia de una clase con otra.

![Clase-03-diagrama-clases.png]

### Resultado

Se espera contar con un script llamado `lista-productos-autos.py` que al ser ejecutado
muestre el resultado siguiente:

```
Clase-02/Proyecto $ python lista-productos-autos.py
---------------------------------------------------------------------
Caja chica             5     100.00     500.00
Caja mediana           3     185.00     555.00
Caja grande            1     299.00     299.00
---------------------------------------------------------------------
                             Total:    1354.00

---------------------------------------------------------------------
VW Vocho (2000)                  1   10000.00   10000.00
Seat Cordoba (2010)              1  185000.00  185000.00
Chevrolet Camaro (2018)          1  299000.00  299000.00
---------------------------------------------------------------------
                                       Total:  494000.00
Clase-02/Proyecto $ 
```
