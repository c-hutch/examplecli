"""Run as CLI"""
from examplecli.util import Util
from examplecli.examplecli import ExampleCli


def main():
    logger = Util().get_logger(__name__)
    logger.debug('main entered')
    ex = ExampleCli()
    try:
        ex.do_something()
    except Exception as e:
        logger.exception("Exception occurred")


if __name__ == '__main__':
    main()
