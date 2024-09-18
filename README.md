# Proyecto de Conexión y Control de PLC con Snap7 y Tkinter

Este proyecto utiliza la librería `snap7` para conectarse y comunicarse con un PLC Siemens S7-1200, y la librería `Tkinter` para mostrar gráficamente el estado del PLC. Además, permite la lectura y escritura de marcas y datos en bloques de datos del PLC.

## Requisitos

Para ejecutar este proyecto, necesitas tener instaladas las siguientes librerías en tu entorno de Python:
- `Python 3.9`: Versión de Python sobre la que funciona correctamente la librería Snap7.
- `snap7`: Biblioteca para la comunicación con PLC Siemens.
- `tkinter`: Biblioteca para la creación de interfaces gráficas (incluida por defecto en Python).

## Contenido de los Archivos

### 1. `plc_gui.py`

Este archivo contiene la lógica de la interfaz gráfica creada con `Tkinter`. Su función principal es permitir la conexión y desconexión del PLC, mostrar el estado (`RUN`, `STOP` o `DESCONOCIDO`) y realizar actualizaciones automáticas del estado del PLC en intervalos configurables por el usuario.

### 2. `plc_read_write.py`

Este archivo permite la lectura y escritura de datos en el PLC. Incluye la funcionalidad para:
- Leer y escribir marcas en el área de memoria del PLC.
- Leer y modificar valores enteros y reales almacenados en los bloques de datos (DB) del PLC.
- Cambiar dinámicamente los valores de las marcas y datos a través de entradas del usuario.

## Funcionalidades

### 1. Interfaz Gráfica de Estado del PLC

La aplicación incluye una interfaz gráfica creada con `Tkinter`, que permite al usuario:

- Conectar al PLC ingresando la dirección IP, el rack y el slot.
- Mostrar el estado del PLC (`RUN`, `STOP` o `DESCONOCIDO`).
- Actualizar automáticamente el estado del PLC a intervalos definidos por el usuario.
- Desconectar del PLC y detener la actualización automática.

### 2. Lectura y Escritura de Datos en el PLC

Además de la interfaz gráfica, se incluye funcionalidad para:

- Leer y escribir marcas en el área de memoria del PLC.
- Leer y escribir datos en bloques de datos (DB) del PLC, como enteros y valores de tipo real.
- Realizar operaciones como cambiar el valor de una marca específica o actualizar el valor de un bloque de datos.

## Instrucciones de Uso

1. Ejecuta el archivo que contiene la interfaz gráfica (`plc_gui.py`).
2. Introduce la IP del PLC, el rack y el slot.
3. Define un intervalo de actualización en segundos.
4. Conéctate al PLC y monitorea su estado desde la interfaz gráfica.
5. Puedes desconectar el PLC y detener la actualización automática en cualquier momento.

### Lectura y Escritura de Marcas y Bloques de Datos

El segundo archivo en este proyecto te permitirá:

- Leer el estado de marcas específicas en el PLC.
- Leer y escribir valores en bloques de datos, como enteros y valores reales.
- Modificar las marcas y los datos de forma dinámica mediante entradas del usuario.

## Consideraciones

- Asegúrate de que el PLC esté accesible en la red con la dirección IP y los parámetros correctos.
- Desactiva el acceso optimizado en los bloques de datos del PLC si es necesario para una correcta lectura y escritura de valores.
- Si el programa es interrumpido, el cliente desconectará automáticamente del PLC.

## Contribuciones

Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request con tus mejoras.

## Licencia

Este proyecto está bajo la Licencia MIT, lo que significa que puedes utilizar, modificar y distribuir el código con libertad,. el autor de la librería Snap7 también tiene Licencia MIT.
