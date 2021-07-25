from .BaseUtil import *


class DeliveryOrder(Base):
    __tablename__ = 'DeliveryOrder'

    id = Column(String(20), primary_key=True)
    plannedDeliveryTime = Column(Date())
    actualDeliveryTime = Column(Date())
    salesOrderId = Column(String(10), ForeignKey('SalesOrder.id'))
    warehouse = Column(String(10), ForeignKey('Warehouse.id'))
    deliveryPhase = Column(Enum('1', '2', '3'))

    def __init__(self, **data):
        self.plannedDeliveryTime = data['plannedDeliveryTime'],
        self.actualDeliveryTime = data['actualDeliveryTime'],
        self.salesOrderId = data['salesOrderId'],
        self.warehouse = data['warehouse'],
        self.deliveryPhase = data['deliveryPhase']

    def __repr__(self):
        return '<DeliveryOrder(id=%r,plannedDeliveryTime=%r,actualDeliveryTime=%r,salesOrderId=%r,warehouse=%r,deliveryPhase=%r)>' \
               % (
                   self.id,
                   self.plannedDeliveryTime,
                   self.actualDeliveryTime,
                   self.salesOrderId,
                   self.warehouse,
                   self.deliveryPhase
               )


class DeliveryItem(Base):
    '''
    发货单物料项
    '''
    __tablename__ = 'DeliveryOrderItem'

    deliveryOrderId = Column(String(10), ForeignKey('DeliveryOrder.id'))
    materialId = Column(String(10), ForeignKey('MaterialDic.id'))
    description = Column(Text())
    amount = Column(Integer())
    unit = Column(String(10))
    pickingStatus = Column(Enum(''))
    pickingAmount = Column(Integer())
    materialState = Column(Enum(''))

    __table_args__ = (
        PrimaryKeyConstraint('deliveryOrderId', 'materialId'),
    )

    def __init__(self, **data):
        self.deliveryOrderId = data['deliveryOrderId'],
        self.materialId = data['materialId'],
        self.description = data['description'],
        self.amount = data['amount'],
        self.unit = data['unit'],
        self.pickingStatus = data['pickingStatus'],
        self.pickingAmount = data['pickingAmount'],
        self.materialState = data['materialState']

    def __repr__(self):
        return '我还没写'
