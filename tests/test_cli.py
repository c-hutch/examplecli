import logging
import pytest
from examplecli import cli


def test_get_args_text_cli():
    cli_args = ['-v', '-t', 'Test Text']
    args = cli.get_args(cli_args=cli_args)
    assert args['text'] == 'Test Text'


def test_get_args_verbose_cli():
    cli_args = ['-v', '-t', 'Test Text']
    args = cli.get_args(cli_args=cli_args)
    assert args['loglevel'] == logging.INFO


def test_get_args_debug_cli():
    cli_args = ['-d', '-t', 'Test Text']
    args = cli.get_args(cli_args=cli_args)
    assert args['loglevel'] == logging.DEBUG


def test_get_args_quiet_cli():
    cli_args = ['-q', '-t', 'Test Text']
    args = cli.get_args(cli_args=cli_args)
    assert args['loglevel'] == logging.ERROR


def test_get_args_text_envvar(monkeypatch):
    cli_args = []
    monkeypatch.setenv('TEXT', 'Test Text')
    args = cli.get_args(cli_args=cli_args)
    assert args['text'] == 'Test Text'


def test_get_args_verbose_envvar(monkeypatch):
    cli_args = []
    monkeypatch.setenv('VERBOSE', 'True')
    args = cli.get_args(cli_args=cli_args)
    assert args['loglevel'] == logging.INFO


def test_get_args_debug_envvar(monkeypatch):
    cli_args = []
    monkeypatch.setenv('DEBUG', 'True')
    args = cli.get_args(cli_args=cli_args)
    assert args['loglevel'] == logging.DEBUG


def test_get_args_quiet_envvar(monkeypatch):
    cli_args = []
    monkeypatch.setenv('QUIET', 'True')
    args = cli.get_args(cli_args=cli_args)
    assert args['loglevel'] == logging.ERROR


def test_get_args_defaults():
    cli_args = []
    args = cli.get_args(cli_args=cli_args)
    assert args['text'] == 'default text'
    assert args['loglevel'] == logging.WARNING


def test_get_args_extra_args_cli():
    cli_args = ['-v', '-t', 'Test Text', 'Too Many args']
    with pytest.raises(SystemExit) as e:
        cli.get_args(cli_args=cli_args)
