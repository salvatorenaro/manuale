
import logging
import sys
from dataclasses import dataclass
import platform


@dataclass
class Security:
    def __init__(self):
        self.REQUIRED_PYTHON_VERSION = (3,6)
    def main(self):
        if sys.version_info < self.REQUIRED_PYTHON_VERSION:
            logging.error('La tua versione è vecchia aggiornala {}'.format(sys.version))
            sys.exit(1)
        else:
            logging.error(f"La tua versione:  {sys.version}")
            sistema_operativo = platform.system().lower()
            if sistema_operativo == 'windows':
                logging.warning(' Benvenuto dal sistema operativo Windows')
            elif sistema_operativo == 'linux':
                logging.warning('Benvenuto dal sistema operativo linux')
            elif sistema_operativo == 'darwin':
                logging.error('Benvenuto da OS')
            else : 
                logging.warning('Benvenuto dal sistema operativo {}'.format(sistema_operativo))



if __name__ == '__main__':
    Security().main()
