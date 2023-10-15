
import os
import sys
import inspect
from datetime import datetime

class ua:

    def ruta_script(self,):
        ruta = os.path.abspath(sys.argv[0])
        return ruta
    
    def nombre_script(self, ruta_logging):
        name_script = ruta_logging.split('/')[-1]
        return name_script
    
    def carpeta_logs(self,ruta_logging, nombre_script):
        ruta = ruta_logging.replace(nombre_script,'')
        ruta_logs = ruta + 'logs'
        if not os.path.exists(ruta_logs):
            os.makedirs(ruta_logs)
        return ruta_logs
    
    def ruta_lanzamientos(self, ):
        frame_info = inspect.stack()[2]
        return frame_info.filename

    def str_time(self,):
        nombre = str(datetime.now()).replace(' ','').replace(':','').replace('.','').replace('-','')
        return nombre