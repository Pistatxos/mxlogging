
## MxLogging

Un sistema de logging optimizado para una interpretación clara y una integración sencilla de mensajes. Pensado para mejorar la trazabilidad y el diagnóstico en proyectos de software.


## USO de mxlogging:

- importar Clase:
import mxlogging

- Llamando a la case:
lgn = mxlogging.lgn()

- Es posible añadir la fecha y hora en el nombre del log en las opciones de config, los log los crea automáticamente dentro de una carpeta llamada logs, que si no existe la creará. El nombre del log es automático con el nombre del script que lo llama. Además en config podemos ajustar si queremos script con nombre único o bien con fecha y hora:
lgn.config(time_log=True) -> Nos creará un log llamado: xxx_fechahora.log
*Si no llamamos a lgn.config -> Nos creará un log llamado: xxx.log

- start prepara el archivo log dentro de la carpeta logs
lgn.start()

- Título: Marca la ruta del script que llama a lgn, válido para cuando cambias de scripts y así localizar bien por donde pasa.
lgn.t()

- Subtitulo: Escribiendo en el log.
lgn.s('Subtitulo')

- Párrafo: Anotaciones dentro de subtitulo, tiene doble espacio para una mejor lectura.
lgn.p('Parrafo')

- Para la gestión de errores:
lgn.e('Errores!')

- Finalizando el logging
lgn.end()


## Ejemplo de un archivo LOG:

15-Oct-23 12:04:43
===============================================================================
    ** START LOG: main.py **
===============================================================================

15-Oct-23 12:04:43
* Ruta script actual:
    /Users/pistatxos/Desktop/carpeta1/test/main.py
-------------------------------------------------------------------------

15-Oct-23 12:04:43 - Subtitulo
15-Oct-23 12:04:43   - Parrafo
15-Oct-23 12:04:43
* Ruta script actual:
    /Users/pistatxos/Desktop/carpeta1/test/main2.py
--------------------------------------------------------------------------

15-Oct-23 12:04:43 - Subtitulo 2
15-Oct-23 12:04:43   - Parrafo 2
15-Oct-23 12:04:43
* Ruta script actual:
    /Users/pistatxos/Desktop/carpeta1/test/main.py
-------------------------------------------------------------------------

15-Oct-23 12:04:43 ERROR - Errores!
15-Oct-23 12:04:43
===============================================================================
    ** FIN LOG: main.py **
===============================================================================
