
import logging
from mxlogging.utils import utils_varios

uv = utils_varios.ua()

class lgn:

    def __init__(self) -> None:
        self.config()

    def config(self, time_log=None) -> None:
        if time_log == None:
            self.time_log = False
        else:
            self.time_log = True
    
    def start(self,) -> None:
        ruta_logging = uv.ruta_script()
        nombre_script = uv.nombre_script(ruta_logging=ruta_logging)
        carpeta_logs = uv.carpeta_logs(ruta_logging=ruta_logging, nombre_script=nombre_script)
        nombre = nombre_script.replace('.py','')
        if self.time_log == True:
            nom_str_time = uv.str_time()
            ruta_nom_logging = carpeta_logs + '/' + nombre + '_' + nom_str_time + '.log'
        else:
            ruta_nom_logging = carpeta_logs + '/' + nombre + '.log'

        logging.basicConfig(filename=ruta_nom_logging, level=logging.INFO, format='%(asctime)s%(message)s', datefmt='%d-%b-%y %H:%M:%S')

        mens = "\n" + "="*80 + f"\n    ** START LOG: {nombre_script} **\n" + "="*80
        logging.info(mens)
        
    def t(self,) -> None:
        ruta_logging = uv.ruta_lanzamientos()
        simbolo = '    ' + '-'*len(ruta_logging)
        mens_up = ' * Ruta script actual:\n' + f'    {ruta_logging}\n' + simbolo
        logging.info(mens_up)

    def s(self, mens) -> None:
        mens_up = f' - {mens}'
        logging.info(mens_up)

    def p(self, mens) -> None:
        mens_up = f'   - {mens}'
        logging.info(mens_up)

    def e(self, mens) -> None:
        mens_up = f' ERROR - {mens}'
        logging.info(mens_up)

    def end(self,) -> None:
        ruta_logging = uv.ruta_script()
        nombre_script = uv.nombre_script(ruta_logging=ruta_logging)
        mens = "\n" + "="*80 + f"\n    ** FIN LOG: {nombre_script} **\n" + "="*80 + '\n\n'
        logging.info(mens)

