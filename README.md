
# MxLogging

### Características Principales:

1. Creación Automática de Archivos: Por defecto, mxlogging crea un archivo .log con el mismo nombre que tu script principal. Además, guarda este archivo en una carpeta llamada "logs". Si la carpeta no existe, la crea automáticamente.
2. Compatibilidad con Otras Bibliotecas: Puedes usar mxlogging sin problemas incluso si ya estás usando otra biblioteca de logging.
3. Múltiples Registros en una Aplicación: Con mxlogging, es fácil tener varios registros en tu aplicación.
    - Nombres Automáticos: Si no especificas un nombre, mxlogging lo genera por ti.
    - Rutas Automáticas: Si no especificas una ruta, mxlogging guarda los archivos .log en la carpeta /logs/.
    - Opción de Registro Único: Si estás creando múltiples registros, puedes optar por unificarlos y almacenarlos en un único archivo .log. (Ver ejemplos más abajo.)
4. Uso Sencillo: Con mxlogging, tu única tarea es escribir el registro. 

## USO de mxlogging:
1. Importar y Crear Instancias de la Clase:
    
    Para empezar, importa la biblioteca y crea una instancia de la clase. Cada instancia corresponde a un registro distinto.
    ```
    import mxlogging 
    lgn = mxlogging.lgn() # Crea una instancia para el primer registro
    ```
    Si deseas tener más registros, puedes crear más instancias:
    ```
    lgn2 = mxlogging.lgn()  # Crea una instancia adicional para otro registro
    ```

2. Configurar mxlogging:

    Cada instancia de registro necesita una configuración. Utiliza el método config para ello.
    ```
    lgn.config(atributos)  # Configura el primer registro
    ```
    Si hemos creado más instancias:
    ```
    lgn2.config(atributos)  # Configura el primer registro
    ```
    * Atributos de configuraciones:
        - time_log
        - time_log = False or None -> crea el archivo log con nombre: nombreScript.log
        - time_log = True -> crea el log crea el archivo log con nombre: nombreScript_fechaHora.log
        - ruta_log
            - ruta_log = None -> crea el archivo en la ruta por default, dentro de una carpeta ./logs en la raiz del script que ejecuta.
            - ruta_log = "path absoluto donde guardará el archivo .log" # Nueva ruta.
        - nombre_log
            - nombre_log = None -> crea el nombre del archivo por defecto que será el nombre del script.
            - nombre_log = "nombreDelLog" # Para renombrar el log.
        - unico_log
            - unico_log = False or None -> Genera varios archivos por separado .log. 
            - unico_log = True -> Genera un único archivo de log con ambos logging registrados.

3. Uso de las Instancias para Registrar:
    
    Después de la configuración, puedes utilizar tus instancias (como lgn o lgn2) para registrar start, mensajes, errores o end.

    - Start:
        lgn.start() -> Prepara el archivo log dentro de la carpeta logs y añade separación start.
        
    - Mensajes:
        - lgn.t() -> Sin añadirle atributos te pone como título la ruta del script, va bien por si quieres anotar cuando cambia de un script a otro el proceso.
        - lgn.s('Mensaje')
        - lgn.p('Mensaje Párrafo (lleva 2 espacios, útil para añadirlo cuando ejecuta dentro de alguna función.)')
        - lgn.e('Mensaje Error, lleva el texto ERROR por defecto.')

    - End:
        - lgn.end() -> Fin del Log, te añade separación para el final.


### Ejemplo de uso de mxlogging:
```
(Ejecutando script main.py)
import mxlogging
lgn = mxlogging.lgn()
lgn.config(time_log=True, 
            ruta_log='/Users/Pistatxos/carpeta1/carpeta2/',
            nombre_log='nombreDelLog')
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
2023-09-15 12:04:43,791 
==============================================================================
    ** START LOG: main.py **
==============================================================================
2023-09-15 12:04:43,791 * Ruta script actual:
    /Users/pistatxos/Desktop/carpeta1/test/main.py
    ----------------------------------------------
2023-09-15 12:04:43,791 - Subtitulo
2023-09-15 12:04:43,791   - Parrafo
2023-09-15 12:04:43,792 * Ruta script actual:
    /Users/pistatxos/Desktop/carpeta1/test/main2.py
    -----------------------------------------------
2023-09-15 12:04:43,792 - Subtitulo 2
2023-09-15 12:04:43,792   - Parrafo 2
2023-09-15 12:04:43,793 * Ruta script actual:
    /Users/pistatxos/Desktop/carpeta1/test/main.py
    ----------------------------------------------
2023-09-15 12:04:43,793 ERROR - Ejemplo Errores!
2023-09-15 12:04:43,793
===============================================================================
    ** FIN LOG: main.py **
===============================================================================
```


### Ejemplo de uso de varios mxlogging en un único archivo:
```
2023-10-29 17:28:05,791 - testing_mxlogging
================================================================================
    ** START LOG: testing_mxlogging.py **
================================================================================
2023-10-29 17:28:05,791 - testing_mxlogging_2
================================================================================
    ** START LOG: testing_mxlogging.py **
================================================================================
2023-10-29 17:28:05,795 - testing_mxlogging * Ruta script actual:
    /Users/pistatxos/Desktop/carpeta1/test/main.py
    ----------------------------------------------
2023-10-29 17:28:05,795 - testing_mxlogging - Subtitulo
2023-10-29 17:28:05,796 - testing_mxlogging   - Parrafo

2023-10-29 17:28:05,796 - testing_mxlogging_2 - Subtitulo 2
2023-10-29 17:28:05,796 - testing_mxlogging_2   - Parrafo 2

2023-10-29 17:28:05,796 - testing_mxlogging ERROR - Ejemplo Errores!
2023-10-29 17:28:05,796 - testing_mxlogging
================================================================================
    ** FIN LOG: testing_mxlogging.py **
================================================================================
```