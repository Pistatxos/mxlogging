
## MxLogging

Un sistema de logging optimizado para una interpretación clara y una integración sencilla de mensajes. Pensado para mejorar la trazabilidad y el diagnóstico en proyectos de software.
Crea con el mismo nombre del script principal el archivo .log y además lo almacena dentro de la carpeta "logs" (si no existe la crea). 
No hay que preocuparse en nada más que de escribir el logging.

## USO de mxlogging:
- Primero importamos y llamamos a la clase:
  import mxlogging -> Importamos clase
  lgn = mxlogging.lgn() -> Llamamos clase

- Añadimos el config del logging:
  lgn.config(atributos)
  * Atributos de configuraciones:
       - time_log = False or None -> crea el archivo log con nombre: nombreScript.log
       - time_log = True -> crea el log crea el archivo log con nombre: nombreScript_fechaHora.log

- Start prepara el archivo log dentro de la carpeta logs y te añade separación start:
  lgn.start()

- Añadir mensajes en LOG:
    - lgn.t() -> Sin añadirle atributos te pone como título la ruta del script, va bien por si quieres anotar cuando cambia de un script a otro.
    - lgn.s('Mensaje Subtitulo')
    - lgn.p('Mensaje Párrafo')
    - lgn.e('Mensaje Error')

- Fin del Log, te añade separación para el final:
    - lgn.end() 


### Ejemplo de uso de mxlogging:
```
(Ejecutando script main.py)
import mxlogging
lgn = mxlogging.lgn()
lgn.config(time_log=True)
lgn.start()

lgn.t()
lgn.s('Subtitulo')
lgn.p('Parrafo')

funcion_main2() # (se llama y ejecuta función del main2.py)
   #(dentro de main2.py)
      #lgn.t()
      #lgn.s('Subtitulo 2')
      #lgn.p('Parrafo 2')

lgn.t()
lgn.e('Ejemplo Errores!')
lgn.end()
```

### Ejemplo archivo LOG creado:
```
-15-Oct-23 12:04:43 
==============================================================================
    ** START LOG: main.py **
==============================================================================
15-Oct-23 12:04:43 * Ruta script actual:
    /Users/pistatxos/Desktop/carpeta1/test/main.py
    ----------------------------------------------
15-Oct-23 12:04:43 - Subtitulo
15-Oct-23 12:04:43   - Parrafo
15-Oct-23 12:04:43 * Ruta script actual:
    /Users/pistatxos/Desktop/carpeta1/test/main2.py
    -----------------------------------------------
15-Oct-23 12:04:43 - Subtitulo 2
15-Oct-23 12:04:43   - Parrafo 2
15-Oct-23 12:04:43 * Ruta script actual:
    /Users/pistatxos/Desktop/carpeta1/test/main.py
    ----------------------------------------------
-15-Oct-23 12:04:43 ERROR - Ejemplo rrores!
15-Oct-23 12:04:43
===============================================================================
    ** FIN LOG: main.py **
===============================================================================
``````