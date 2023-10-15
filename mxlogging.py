
import logging
import utils.utils_varios

uv = utils.utils_varios.ua()

class lgn:

    def __init__(self) -> None:
        self.config()

    def config(self, time_log=None) -> None:
        if time_log == None:
            self.time_log = False
        else:
            self.time_log = True
    
    def start(self,):
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

        mens = f'''
===============================================================================
    ** START LOG: {nombre_script} **
===============================================================================
'''
        logging.info(mens)
        

    def t(self,):
        #ruta_logging = uv.ruta_script()
        ruta_logging = uv.ruta_lanzamientos()
        simbolo = '-'*len(ruta_logging)+'----'
        mens_up = f'''
* Ruta script actual:
    {ruta_logging}
{simbolo}
'''
        logging.info(mens_up)

    def s(self, mens):
        mens_up = f' - {mens}'
        logging.info(mens_up)

    def p(self, mens):
        mens_up = f'   - {mens}'
        logging.info(mens_up)

    def e(self, mens):
        mens_up = f' ERROR - {mens}'
        logging.info(mens_up)

    def end(self,):
        ruta_logging = uv.ruta_script()
        nombre_script = uv.nombre_script(ruta_logging=ruta_logging)
        mens = f'''
===============================================================================
    ** FIN LOG: {nombre_script} **
===============================================================================


'''
        logging.info(mens)

