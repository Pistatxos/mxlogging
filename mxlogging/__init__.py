
import logging
from mxlogging.utils import utils_varios

uv = utils_varios.ua()

class lgn:

    def __init__(self) -> None:
        '''Inicia con las configuraciones del usuario.'''
        self.config()

    def config(self, time_log=None, ruta_log=None, nombre_log=None, unico_log=None) -> None:
        '''Atributos con los ajustes modificables:
            -time_log: Añade al nombre del log "_fechaHoraSegMilseg.log". Pasar -> True o False
            -ruta_log: Para elegir nueva ruta para guardar el log. Pasar ->  Ruta absoluta.
            -nombre_log: Para elegir nuevo nombre del log. Pasar ->  Nombre para el log.
            -unico_log: En caso de generar varios log en un mismo script puedes escribirlo todo en uno. Pasar ->  True o False.
        '''
        if time_log == None:
            self.time_log = False
        else:
            self.time_log = True
        if ruta_log == None:
            self.ruta_log = None
        else:
            self.ruta_log = ruta_log
        if nombre_log == None:
            self.nombre_log = None
        else:
            self.nombre_log = nombre_log
        if unico_log == None:
            self.unico_log = False
        else:
            self.unico_log = True

    def start(self,) -> None:
        '''Genera el loggin y añade las funciones del LOG.'''
        ruta_logging = uv.ruta_script()
        nombre_script = uv.nombre_script(ruta_logging=ruta_logging)

        ## Configuraciones extra:
        ## Si tiene ruta en config la usamos, sino creamos la carpeta
        if self.ruta_log != None:
            carpeta_logs = self.ruta_log
        else:
            carpeta_logs = uv.carpeta_logs(ruta_logging=ruta_logging, nombre_script=nombre_script)
        ## Añadir manual nombre log
        if self.nombre_log == None:
            nombre = nombre_script.replace('.py','')
        else:
            nombre = str(self.nombre_log).replace('.log','')
        ## Añadir FechaHora al archivo .log
        if self.time_log == True:
            nom_str_time = uv.str_time()
            ruta_nom_logging = carpeta_logs + '/' + nombre + '_' + nom_str_time + '.log'
        else:
            ruta_nom_logging = carpeta_logs + '/' + nombre + '.log'

        ## Creación tipo logging Multiversión
        cont = 2
        if self.unico_log:
            # Crea los nombres para el distinguirlos en un mismo log.
            while nombre in logging.Logger.manager.loggerDict:
                nombre = nombre + f'_{cont}'
                cont += 1
        else:
            # Comprobar si ya existe un FileHandler con ese nombre de alog y si es así le suma nº al nombre.
            while nombre in logging.Logger.manager.loggerDict or ruta_nom_logging in [handler.baseFilename for handler in logging._handlers.values() if isinstance(handler, logging.FileHandler)]:
                nombre = nombre.split('_')[0] + f'_{cont}'
                base_filename = ruta_nom_logging.replace('.log', '')
                ruta_nom_logging = base_filename + f'_{cont}.log'
                cont += 1


        self.logg = logging.getLogger(nombre)
        self.logg.setLevel(logging.INFO)


        if not self.logg.handlers:
            # Configura un manejador para escribir logs en un archivo dependiendo si es unico
            file_handler = logging.FileHandler(ruta_nom_logging)
            if self.unico_log:
                # Si es unico añade el nombre de quien envia el log.
                formatter = logging.Formatter('%(asctime)s - {}%(message)s'.format(nombre))
            else:
                # Si es con archivos separdos o solo hay un log lo creará normal.
                formatter = logging.Formatter('%(asctime)s %(message)s')

            file_handler.setFormatter(formatter)

            # Añadir el manejador al logger
            self.logg.addHandler(file_handler)

        mens = "\n" + "="*80 + f"\n    ** START LOG: {nombre_script} **\n" + "="*80
        self.logg.info(mens)
        
    def t(self,) -> None:
        '''Crea mensaje con ruta del script que lo ejecuta.'''
        ruta_logging = uv.ruta_lanzamientos()
        simbolo = '    ' + '-'*len(ruta_logging)
        mens_up = ' * Ruta script actual:\n' + f'    {ruta_logging}\n' + simbolo
        self.logg.info(mens_up)

    def s(self, mens) -> None:
        '''Crea mensaje.'''
        mens_up = f' - {mens}'
        self.logg.info(mens_up)

    def p(self, mens) -> None:
        '''Crea mensaje con doble espacio para distinguir.'''
        mens_up = f'   - {mens}'
        self.logg.info(mens_up)

    def e(self, mens) -> None:
        '''Crea mensaje con levelname ERROR directamente.'''
        mens_up = f' ERROR - {mens}'
        self.logg.info(mens_up)

    def end(self,) -> None:
        '''Finaliza el log con cartel final.'''
        ruta_logging = uv.ruta_script()
        nombre_script = uv.nombre_script(ruta_logging=ruta_logging)
        mens = "\n" + "="*80 + f"\n    ** FIN LOG: {nombre_script} **\n" + "="*80 + '\n\n'
        self.logg.info(mens)

