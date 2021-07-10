from BaseUtil import *
from dataclasses import dataclass


class MaterialDic(Base):
    __tablename__ = 'MaterialDic'

    id = Column(String(10), primary_key=True)
    name = Column(Text())
    price = Column(Float())

    def __init__(self, *args, **kwargs):
        print('dasfasdf')
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.price = kwargs['price']

    def __repr__(self):
        return "<MaterialDic(id='%r',name='%r',price='%r')>" % (self.id, self.name, self.price)


class Warehouse(Base):
    __tablename__ = 'Warehouse'
    id = Column(String(10), primary_key=True)
    name = Column(String(50))


class Inventory(Base):
    __tablename__ = 'Inventory'
    warehouseId = Column(String(10), ForeignKey('Warehouse.id'))
    materialDicId = Column(String(10), ForeignKey('MaterialDic.id'))
    volume = Column(Float())
    requestVolume = Column(Float())
    onOrderStock = Column(Float())
    __table_args__ = (
        PrimaryKeyConstraint('warehouseId', 'materialDicId'),
    )
