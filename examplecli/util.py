"""utilities file"""
import logging


class Util:
    """ Utilities class
    """
    @staticmethod
    def get_logger(name):
        """
        Get a logging.logger and set its logging handlers, log to a file and the console
        :param self:
        :param name: the string name of the logger
        :return: a logging.Logger object
        """
        logger = logging.getLogger(name)
        # TODO: move logging config into file
        if not logger.handlers:
            logger.setLevel(logging.WARNING)
            # set format
            fmt = logging.Formatter(fmt='%(levelname)s - %(asctime)s - %(process)s - %(message)s',
                                    datefmt='%d-%b-%y %H:%M:%S')
            # add stream logging
            l_handler = logging.StreamHandler()
            l_handler.setFormatter(fmt)
            logger.addHandler(l_handler)
            # add file logging
            f_handler = logging.FileHandler(filename='examplecli.log', mode='a')
            f_handler.setFormatter(fmt)
            logger.addHandler(f_handler)
        return logger


