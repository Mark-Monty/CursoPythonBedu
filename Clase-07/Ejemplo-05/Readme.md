`Fullstack con Python` > [`Backend con Python`](../../Readme.md) > [`Sesión 07`](../Readme.md) > Ejemplo-05

## Conociendo los micro frameworks creando una micro aplicación web con Bottle.

### OBJETIVOS
- Conocer el flujo de información entre una petición GET desde el Navegador hasta la aplicación web creada usando el micro framework Bottle.

#### REQUISITOS
1. Actualizar repositorio

#### DESARROLLO
1. Entendiendo a los frameworks: Creando la aplicación web `webapp/index.py` que muestre un formulario donde se capturen dos campos, email y contraseña, el formulario sea enviado se mostrará un mensaje indicando los campos capturados.

   __Cambiarse a la carpeta `webapp`:__
   ```console
   Clase-07/Ejemplo-05 $ cd webapp
   Clase-07/Ejemplo-05/webapp $
   ```

   __Ejecutando el script con:__

   ```console
   Clase-07/Ejemplo-05/webapp $ python index.py
   Bottle v0.13-dev server starting up (using WSGIRefServer())...
   Listening on http://localhost:8000/
   Hit Ctrl-C to quit.
   ```

   Se puede acceder abriendo la siguiente url en algún navegador:
   - http://localhost:8000
