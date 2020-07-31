import logging

class Log(object):

    def __init__(self):
        logging.basicConfig(format="%(levelname)s:%(filename)s:%(lineno)d: --> %(message)s")
        self.logger = logging.getLogger("core")
        self.logger.setLevel(10)
    def info(self, msg):
        self.logger.info(msg)
    def debug(self, msg):
        self.logger.debug(msg)
    def waring(self, msg):
        self.logger.waring(msg)
log = Log()