from examplecli.util import Util
import logging


def test_constructor():
    utilities = Util()
    assert isinstance(utilities, Util)


def test_get_logger():
    logger = Util().get_logger('test')
    assert isinstance(logger, logging.Logger)


def test_logger_has_handlers():
    logger = Util().get_logger('test')
    assert logger.hasHandlers()

