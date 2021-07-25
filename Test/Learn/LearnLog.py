import logging
from logging.handlers import RotatingFileHandler

from colorlog import ColoredFormatter

ErpLogger = logging.getLogger('autotest')
ErpLogger.setLevel(logging.DEBUG)

fmt = '%(log_color)s%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s'

datefmt = '%b %d  %Y %H:%M:%S'

log_colors = {'DEBUG': 'blue', 'INFO': 'green', 'WARNING': 'red', 'ERROR': 'red,bg_black'}
formatter = ColoredFormatter(fmt=fmt, datefmt=datefmt, log_colors=log_colors, reset=True, secondary_log_colors={},
                             style='%')


hd_1 = logging.StreamHandler()
hd_1.setFormatter(formatter)

ErpLogger.addHandler(hd_1)
ErpLogger.error('21222')
ErpLogger.warning('3213123')
ErpLogger.debug('asdfasdf')
ErpLogger.info('dfasd sdaf')
