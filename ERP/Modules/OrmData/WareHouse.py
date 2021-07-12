from .BaseUtil import *


class MaterialDic(Base):
    '''
    可以更改的
    '''
    __tablename__ = 'MaterialDic'

    id = Column(String(10), primary_key=True)
    name = Column(Text())
    price = Column(Float())

    def __init__(self, *args, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.price = kwargs['price']

    def __repr__(self):
        return "<MaterialDic(id=%r,name=%r,price=%r)>" % (self.id, self.name, self.price)


class Warehouse(Base):
    __tablename__ = 'Warehouse'
    id = Column(String(10), primary_key=True)
    name = Column(String(50))

    def __init__(self, **data):
        self.id = data['id']
        self.name = data['name']

    def __repr__(self):
        return '<Warehouse()>'


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

    def __init__(self, **kwargs):
        self.warehouseId = kwargs['warehouseId']
        self.materialDicId = kwargs['materialDicId']
        self.volume = kwargs['volume']
        self.requestVolume = kwargs['requestVolume']
        self.onOrderStock = kwargs['onOrderStock']

    def __repr__(self):
        return "<Inventory(warehouseId='%r',materialDicId='%r',volume='%r',requestVolume=%r,onOrderStock=%r)>" % (
            self.name,
            self.price,
            self.volume,
            self.requestVolume,
            self.onOrderStock)
