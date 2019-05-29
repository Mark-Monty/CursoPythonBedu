##### RETO-02
## INICIALIZANDO LA BASE DE DATOS EN MARIADB

### OBJETIVO
Realizar el procedimiento en un servidor MySQL para inicializar la base de datos haciendo uso de contenedores.

#### REQUISITOS
1. Contar con Docker instalado
2. Haber actualizado el contenido de la carpeta `CursoPythonBedu`
3. Abrir una terminal o consola de comandos y cambiarse a la carpeta de trabajo `CursoPythonBedu/Clase-05/Reto-02` y observar que exista el archivo `bedutravels.sql`

   ```sh
   $ cd Clase-05/Reto-02

   Clase-05/Reto-02 $ ls
   bedutravels.sql  Readme.md

   Clase-05/Reto-02 $
   ```
   ***

### DESARROLLO
1. Para poder hacer uso del servidor MariaDB por medio de Docker, lo primero que hay que hacer es descargar un archivo llamado imagen que contiene ya instalado MariaDB y usaremos la versión 10.3 por lo que usaramos el siguiente comando:

   __Resultado__

   Como la imagen ya se descargó para el __Ejemplo-02__ no es necesario descargarla nuevamente, con una vez es suficiente.
   ***

2. Iniciando un servidor de MariaDB 10.3 creando un contenedor de Docker llamado __pythonsql__ (--name) y asignando una clave __pythonsql__ (MYSQL_ROOT_PASSWORD) al usuario __root__

   __Resultado__

   El contenedor de Docker iniciando en el __Ejemplo-02__ con el servidor MariaDB, es un servidor que se puede usar para todos los proyectos de esta clase y no es necesario crearlo ni iniciarlo nuevamente.
   ***

5. Los datos para la conexión al servidor MariaDB también son los mismos:
   - __Host:__ localhost
   - __User:__ root
   - __Pass:__ pythonsql
   ***

6. Para inicializar la base de datos se ejecuta el comando `mysql` pero desde el contenedor de Docker con el siguiente comando:
   ```sh
   ???
   ```
   ***

7. Para validar que la base de datos se haya inicializado de forma correcta se realiza una conexión a la base de datos BeduTravels usando los datos:

   - __Host:__ localhost
   - __User:__ BeduTravels
   - __Pass:__ BeduTravels
   - __Base de datos:__ BeduTravels

  ```sh
  Clase-05/Reto-02 $ ???

  MariaDB [BeduTravels]> SHOW TABLES;
  Empty set (0.000 sec)

  MariaDB [BeduTravels]> EXIT;

  Clase-05/Reto-02 $
  ```
  ***

Si has llegado hasta este punto __FELICIDADES__, toma __otro__ respiro o ayuda a algún compañero que no lo haya logrado aún o tomate un café te lo mereces.
