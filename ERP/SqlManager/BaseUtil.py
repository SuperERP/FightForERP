from sqlalchemy import *
# import DataClass
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
# engine = create_engine('sqlite:///tutorial.db', echo=True)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base(engine)  # SQLORM基类
session = sessionmaker(engine)()  # 构建session对象


