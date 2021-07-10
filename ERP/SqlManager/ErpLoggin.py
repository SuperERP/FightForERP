import logging
from logging.handlers import RotatingFileHandler

from colorlog import ColoredFormatter

ErpLogger = logging.getLogger('autotest')
ErpLogger.setLevel(logging.DEBUG)

fmt = '%(log_color)s%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s'

datefmt = '%b %d  %Y %H:%M:%S'

log_colors = {
    'DEBUG': 'blue',
    'INFO': 'green',
    'WARNING': 'red',
    'ERROR': 'red,bg_black'
}
formatter = ColoredFormatter(fmt=fmt, log_colors=log_colors, reset=True, secondary_log_colors={},
                             style='%')
log_path = '/home/supercb/PycharmProjects/myERP/erp'
log_name = log_path + '.log'
logfile = log_name
fh = logging.FileHandler(logfile, mode='w')
# fh.setFormatter(formatter)

hd_1 = logging.StreamHandler()
hd_1.setFormatter(formatter)

ErpLogger.addHandler(hd_1)
ErpLogger.addHandler(fh)
