"""utilities file"""
import logging


class ExampleCli:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def do_something(self):
        self.logger.debug('do_something called')
