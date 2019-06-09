"""Run CLI"""
import os
import sys
import argparse
import logging.config
import yaml

from examplecli.examplecli import MyClass


def get_args(cli_args):
    """Get the arguments required for the command.  Check for cli args if none supplied
    then check for env vars.  Use cli args or env vars, not both.
    :param cli_args: list of cli arguments from sys.argv[0:]
    :return: dictionary containing the parsed arguments
    """

    if len(cli_args) > 0:
        # cli arguments provided
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-d",
            "--debug",
            action="store_const",
            dest="loglevel",
            const=logging.DEBUG,
            default=logging.WARNING,
            help="show debug messages",
        )
        parser.add_argument(
            "-v",
            "--verbose",
            action="store_const",
            dest="loglevel",
            const=logging.INFO,
            help="show informational messages",
        )
        parser.add_argument(
            "-q",
            "--quiet",
            action="store_const",
            dest="loglevel",
            const=logging.ERROR,
            help="show error messages only",
        )
        parser.add_argument(
            "-t",
            "--text",
            default="default text",
            help="example text argument for the app",
        )

        args = vars(parser.parse_args(cli_args))
    else:
        # check for env var settings
        # TODO: refactor this into a 'LOGLEVEL' envvar with level value i.e LOGLEVEL=DEBUG?
        if os.getenv("VERBOSE"):
            args = {"loglevel": logging.INFO}
        elif os.getenv("DEBUG"):
            args = {"loglevel": logging.DEBUG}
        elif os.getenv("QUIET"):
            args = {"loglevel": logging.ERROR}
        else:
            args = {"loglevel": logging.WARNING}
        args["text"] = os.getenv("TEXT", "default text")

    return args


def get_logger_yaml():
    with open("logconfig.yaml", "rt") as f:
        config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
    return logging.getLogger("examplecli")


def main():
    """
    Main example cli function
    :return: None
    """
    logger = get_logger_yaml()
    cli_args = get_args(cli_args=sys.argv[1:])
    logger.setLevel(cli_args["loglevel"])
    logger.debug(f"log level set: {logger.getEffectiveLevel()}")
    ex = MyClass(**cli_args)
    ex.do_something()


if __name__ == "__main__":
    main()
