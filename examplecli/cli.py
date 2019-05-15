"""Run as CLI"""
import os
import sys
import argparse
import logging

from examplecli.util import Util
from examplecli.examplecli import ExampleCli


def get_args(cli_args):
    """Get the arguments required for the command.  Check for cli args first, if none supplied
    then check for env vars.
    :param cli_args: list of cli arguments from sys.argv[1:]
    :return: an argparse.Namespace containing the parsed arguments
    """

    print(f'sys argv is {sys.argv[0]}')
    if len(cli_args) > 1:
        # cli arguments provided
        parser = argparse.ArgumentParser()
        level_group = parser.add_mutually_exclusive_group()
        level_group.add_argument('-v', '--verbose', action='store_true')
        level_group.add_argument('-q', '--quiet', action='store_true')
        parser.add_argument('-t', '--text', default='default text', help='increase output verbosity')
        args = vars(parser.parse_args(cli_args))
    else:
        # check for env var settings
        args = {'verbose': os.getenv('VERBOSE', False),
                'quiet': os.getenv('QUIET', False),
                'text': os.getenv('TEXT', 'default text'),
                }
    return args


def get_env_args():
    """Check environment variables for arguments, used for running in a container"""


def set_logger_level(logger, args):
    """
    Set the logging level
    :param logger: The base logger
    :param args: dict containing arguments
    :return: None
    """

    if args['verbose']:
        logger.setLevel(logging.DEBUG)
        logger.debug('verbose logging enabled')
    elif args['quiet']:
        logger.setLevel(logging.ERROR)
    else:
        logger.setLevel(logging.WARNING)


def main():
    """
    Main example cli function
    :return: None
    """
    logger = Util().get_logger(__name__)
    logger.debug('main entered')
    try:
        args = get_args(cli_args=sys.argv[1:])
        logger.debug(args)
        set_logger_level(logger, args)
        ex = ExampleCli()
        ex.do_something()
    except Exception as e:
        logger.exception('Exception occurred')


if __name__ == '__main__':
    main()
