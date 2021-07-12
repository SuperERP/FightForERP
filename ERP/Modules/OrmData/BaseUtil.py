from sqlalchemy import *
# import DataClass
engine = create_engine("sqlite+pysqlite:///:memory:",echo=True, future=True)
# engine = create_engine('sqlite:///tutorial.db', echo=True)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base(engine)  # SQLORM基类
session = sessionmaker(engine)()  # 构建session对象

import logging
from logging.handlers import RotatingFileHandler
import socket
from colorlog import ColoredFormatter

hostname = socket.gethostname()
# session.add(
#     Inquiry(**data),
# )
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
