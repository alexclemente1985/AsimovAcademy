import logging
import os


def modulo_logging():
    try:
        LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
        cwd = os.path.join(os.getcwd(),'logs')

        log_file = os.path.join(cwd, "modulo_logging.log")
        logging.basicConfig(filename=log_file, level=logging.DEBUG, format=LOG_FORMAT)
        log = logging.getLogger()

        log.info("TESTE LOG")
        log.critical("Erro grave")
        log.error("Erro no programa")
        log.debug("Teste debug")
        log.warning(("WARNING!"))
        log.level

    except Exception as e:
        print("Erro na criação/manipulação do log: ", e)



if __name__ == '__main__':
    modulo_logging()