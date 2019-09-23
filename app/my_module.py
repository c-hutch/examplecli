"""sample module"""
import logging


class MyWork:
    def __init__(self, **kwargs):
        self.logger = logging.getLogger(__name__)
        self.kwargs = kwargs

    def do_something(self):
        self.logger.debug(f"do_something called with kwargs = {self.kwargs}")
