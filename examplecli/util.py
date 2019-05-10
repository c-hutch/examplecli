import logging


class Util:

    def get_logger(self, name):
        logger = logging.getLogger(name)
        if not logger.handlers:
            logger.setLevel(logging.DEBUG)
            fmt = logging.Formatter(fmt='%(levelname)s - %(asctime)s - %(process)s - %(message)s',
                                    datefmt='%d-%b-%y %H:%M:%S')
            # add formatter
            l_handler = logging.StreamHandler()
            l_handler.setFormatter(fmt)
            logger.addHandler(l_handler)
            # log to file
            f_handler = logging.FileHandler(filename='examplecli.log', mode='a')
            f_handler.setFormatter(fmt)
            logger.addHandler(f_handler)
        return logger
