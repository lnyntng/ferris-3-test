import ferris3
import logging


@ferris3.auto_service
class RegiService(ferris3.Service):

    @ferris3.auto_method
    def hello(self, request):
        logging.info("Hello, is it me you're looking for?")
