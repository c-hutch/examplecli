"""Run as CLI"""
import os
import sys
import argparse
import logging.config
import yaml

from examplecli.examplecli import ExampleCli


def get_args(cli_args):
    """Get the arguments required for the command.  Check for cli args if none supplied
    then check for env vars.
    :param cli_args: list of cli arguments from sys.argv[1:]
    :return: an argparse.Namespace containing the parsed arguments
    """

    if len(cli_args) > 1:
        # cli arguments provided
        parser = argparse.ArgumentParser()
        parser.add_argument('-d', '--debug',
                            action="store_const",
                            dest="loglevel",
                            const=logging.DEBUG,
                            default=logging.WARNING,
                            help='show debug messages',
                            )
        parser.add_argument('-v', '--verbose',
                            action="store_const",
                            dest="loglevel",
                            const=logging.INFO,
                            help='show informational messages',
                            )
        parser.add_argument('-q', '--quiet',
                            action="store_const",
                            dest="loglevel",
                            const=logging.ERROR,
                            help='show error messages only',
                            )
        parser.add_argument('-t', '--text', default='default text', help='example text argument for the app')

        args = vars(parser.parse_args(cli_args))
    else:
        # check for env var settings
        if os.getenv('VERBOSE'):
            args = {'loglevel': logging.INFO}
        elif os.getenv('DEBUG'):
            args = {'loglevel': logging.DEBUG}
        elif os.getenv('QUIET'):
            args = {'loglevel': logging.ERROR}
        else:
            args = {'loglevel': logging.WARNING}
        args['text'] = os.getenv('TEXT', 'default text')

    return args


def get_logger_yaml():
    with open('logconfig.yaml', 'rt') as f:
        config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
    return logging.getLogger('examplecli')


def main():
    """
    Main example cli function
    :return: None
    """
    # logger = Util().get_logger('examplecli')
    logger = get_logger_yaml()
    try:
        args = get_args(cli_args=sys.argv[1:])
        logger.setLevel(args['loglevel'])
        logger.debug(f'cli args: {args}')
        ex = ExampleCli()
        ex.do_something()
    except Exception as e:
        logger.exception('Exception occurred')


if __name__ == '__main__':
    main()
