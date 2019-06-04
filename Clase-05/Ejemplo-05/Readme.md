##### EJEMPLO-05
## CRUD DE DATOS CON PYTHON EN MYSQL

### OBJETIVO
Conocer el procedimiento para realizar un CRUD de datos a una tabla en un servidor MariaDB desde Python.

#### REQUISITOS
1. Contar con los datos de conexión a la base de datos Biblioteca.

   __Host:__ localhost
   __User:__ Biblioteca \
   __Password:__ Biblioteca \
   __Base de datos:__ Biblioteca

1. Contar con la tabla __Libro__ creada y con datos muestra en la base de datos:

  ![Tabla Libro](assets/tabla-libro.jpg)

1. Usar la carpeta de trabajo `Clase-05/Ejemplo-04`

   ```sh
   $ cd Clase-05/Ejemplo-05

   Clase-05/Ejemplo-05 $
   ```

1. Instalar el módulo `mysql-connector-python` que será el responsable de permitir realizar una conexión a base de datos MySQL / MariaDB desde Python.

   __Sito principal:__
   https://dev.mysql.com/doc/connector-python/en/

   __Instalación con el comando pip:__
   ```sh
   $ pip install mysql-connector-python
   Collecting mysql-connector-python
   Using cached https://files.pythonhosted.org/packages/43/bd/43a128bbd6a3237d6f255c7afaa9308430d5c90f8db8371276169722f037/mysql_connector_python-8.0.16-cp37-cp37m-manylinux1_x86_64.whl
   Requirement already satisfied: protobuf>=3.0.0 in /home/rctorr/miniconda3/lib/python3.7/site-packages (from mysql-connector-python) (3.7.1)
   Requirement already satisfied: six>=1.9 in /home/rctorr/miniconda3/lib/python3.7/site-packages (from protobuf>=3.0.0->mysql-connector-python) (1.12.0)
   Requirement already satisfied: setuptools in /home/rctorr/miniconda3/lib/python3.7/site-packages (from protobuf>=3.0.0->mysql-connector-python) (41.0.0)
   Installing collected packages: mysql-connector-python
   Successfully installed mysql-connector-python-8.0.16

   $
   ```

### DESARROLLO
1. __OPERACIÓN READ__ Crea el script `lista-registros.py` que imprima en formato texto en la salida estándar la lista de registros de la tabla proporcionada como parámetro en la línea de comandos. Hacer uso de los módulos `click`, `mysql-connector-python` y `stdout`.

   __Caso: Ejecutando el script sin argumentos__

   ```sh
   Clase-05/Ejemplo-05 $ python lista-registros.py

   Tablas disponibles
   ------------------
   Libro
   ------------------
   ```

   __Caso: Imprimiendo registros de la tabla Libro__

   ```sh
   Clase-05/Ejemplo-05 $ python lista-registros.py Libro

   Tabla: Libro
   ------------
   Id | Titulo                 | Editorial   | NumPag | Autores
    1 | Yo, Robot              | Gnome Press |    374 |       1
    2 | El fin de la eternidad | Gnome Press |    191 |       1
    3 | El arte de la guerra   | Obelisco    |    112 |       2
   ------------
   ```
   ***

__Nota:__ En la carpeta ya existe el script `stdout.py` que es un módulo que contiene la función `imprime_registros()` que imprime una lista de registros con un título, se puede consultar la ayuda desde ipython.


### SOLUCIÓN DE PROBLEMAS

1. Error al conectarse desde el script `lista-registros.py` al contenedor `pythonsql` usando la dirección IP en equipos con Mac y Windows.

   __Descripción__: El script `modelomysql.py` se ha modificado para que haga uso de la dirección IP del contenedor __pythonsql__ que en la mayoría de los casos ha resultado ser 172.17.0.2 y tras ejecutar el script en Python se obtiene el siguiente error en los equipos con Mac y Windows:
   ```
   Clase-05/Ejemplo-05 $ python lista-registros.py
   2003 (HY000): Can't connect to MySQL server on '172.17.0.2' (113)

   Tablas disponibles
   ------------------
   ------------------

   Clase-05/Ejemplo-05 $
   ```
   Este error se presenta debido a que tanto en Mac como en Windows la implementación de Docker no permite realizar esa conexión en base a la dirección IP (en Linux todo se puede!), eso está documentado y se puede revisar en el siguiente enlace:

   https://docs.docker.com/docker-for-mac/networking/

   Y en ese mismo enlace se mencionan dos posibles soluciones y una de ellas se describe a continuación.

   __Solución:__
   1. Eliminar el contenedor __pythonsql__:
   ```bash
   $ docker stop pythonsql  # se detiene el contenedor antes de borrarlo
   $ docker rm pythonsql  # se elimina el contenedor definitivamente
   ```
   1. Crear el contenedor nuevamente con el mismo nombre __pythonsql__ y clave para el usuario root:
   ```bash
   $ docker create --name pythonsql -e MYSQL_ROOT_PASSWORD=pythonsql -p 3306:3306 mariadb:10.3
   46304152770a2e37d01fcbd861eda3ec7d71352b5b08ca7d3ec1cde5cffc885f
   $
   ```
   Recordar que el contenedor ejecuta el servidor MariaDB, que activa el puerto 3306 para recibir peticiones de los clientes, ahora se ha agregado la opción `-p 3306:3306` que activa el mismo puerto 3306 pero en nuestro equipo local, por lo ya no es necesario ocupar la dirección IP del contenedor, si no que podemos usar nuevamente __localhost__ como nombre de host.
   1. Iniciar el contenedor:
   ```bash
   $ docker start pythonsql
   pythonsql
   $
   ```
   1. Cambiarse a la carpeta del Ejemplo-05 de la Clase-05:
   ```bash
   $ cd Clase-05/Ejemplo-05
   Clase-05/Ejemplo-05 $
   ```
   1. Se crea la base de datos para la Biblioteca nuevamente usando los datos de conexión para el usuario __root__:
   ```bash
   Clase-05/Ejemplo-05 $ docker exec -i pythonsql mysql -uroot -ppythonsql < sql/biblioteca.sql
   ```
   1. Se inicializa la base de datos usando los datos de conexión para el usuario __Biblioteca__:
   ```bash
   Clase-05/Ejemplo-05 $ docker exec -i pythonsql mysql -uBiblioteca -pBiblioteca Biblioteca < sql/tabla-libro.sql
   ```
   1. Modificar nuevamente el script `modulomysql.py` para que la variable `host` tenga el valor de `localhost` nuevamente.

   1. Ejecutar el script en Python que deberá de obtener el resultado siguiente:

    ```bash
    Clase-05/Ejemplo-05 $ python lista-registros.py Libro
    Tabla: Libro
    ------------
    Id | Titulo                 | Editorial   | Numpag | Autores
     1 | Yo, Robot              | Gnome Press |    374 |       1
     2 | El fin de la eternidad | Gnome Press |    191 |       1
     3 | El arte de la guerra   | Obelisco    |    112 |       2
    ------------
    ```
