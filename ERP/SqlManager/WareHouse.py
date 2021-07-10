from BaseUtil import *


class MaterialDic(Base):
    __tablename__ = 'MaterialDic'
    id = Column(String(10), primary_key=True)
    name = Column(Text())
    price = Column(Float())

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
