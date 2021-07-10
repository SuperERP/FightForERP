from BaseUtil import *


class Delivery(Base):
    __tablename__ = 'Delivery'
    id = Column(String(10), primary_key=True)
    plannedDeliveryTime = Column(Date())
    actualDeliveryTime = Column(Date())
    salesOrderId = Column(String(10), ForeignKey('Salesorder.id'))
    warehouse = Column(String(10), ForeignKey('Warehouse.id'))
    deliveryPhase = Column(Enum('1', '2', '3', '4', '5'))


class DeliveryItem(Base):
    __tablename__ = 'DeliveryItem'
    deliveryId = Column(String(10), ForeignKey('Delivery.id'))
    materialId = Column(String(10), ForeignKey('MaterialDic.id'))
    description = Column(Text())
    amount = Column(Integer())
    unit = Column(String(10))
    pickingStatus = Column(Enum(''))
    pickingAmount = Column(Integer())
    materialState = Column(Enum(''))
    __table_args__ = (
        PrimaryKeyConstraint('deliveryId', 'materialId'),
    )
