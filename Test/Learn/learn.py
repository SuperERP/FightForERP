from sqlalchemy import *
# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
engine = create_engine('sqlite:///tutorial.db',echo=True)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

# engine = create_engine(DB_URI)
Base = declarative_base(engine)  # SQLORM基类
session = sessionmaker(engine)()  # 构建session对象


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    type = Column(String(20))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'employee'
    }


class Manager(Employee):
    manager_data = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'manager'
    }


class Engineer(Employee):
    engineer_info = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'engineer'
    }


Base.metadata.create_all()  # 将模型映射到数据库中
session.add_all([
    Employee(id=10, name='dasf', type='engineer')
])
session.commit()
