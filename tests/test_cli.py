import argparse
import logging
import pytest
from examplecli import cli


def test_get_args_text():
    cli_args = ['-v', '-t', 'Test Text']
    args = cli.get_args(cli_args=cli_args)
    assert args['text'] == 'Test Text'
    assert args['verbose'] is True
    assert args['quiet'] is False


def test_get_args_extra_args():
    cli_args = ['-v', '-t', 'Test Text', 'Too Many args']
    with pytest.raises(SystemExit) as e:
        cli.get_args(cli_args=cli_args)


def test_get_args_defaults():
    cli_args = {}
    args = cli.get_args(cli_args=cli_args)
    assert args['text'] == 'default text'
    assert args['verbose'] is False
    assert args['quiet'] is False


def test_set_logger_level_verbose():
    args = vars(argparse.Namespace(quiet=False, verbose=True, text='test'))
    logger = logging.getLogger('pytest')
    cli.set_logger_level(logger, args)
    assert logger.level == logging.DEBUG


def test_set_logger_level_quiet():
    args = vars(argparse.Namespace(quiet=True, verbose=False, text='test'))
    logger = logging.getLogger('pytest')
    cli.set_logger_level(logger, args)
    assert logger.level == logging.ERROR


def test_set_logger_level_default():
    args = vars(argparse.Namespace(quiet=False, verbose=False, text='test'))
    logger = logging.getLogger('pytest')
    cli.set_logger_level(logger, args)
    assert logger.level == logging.WARNING
