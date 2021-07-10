from ERP.SqlManager.BaseUtil import *

from ERP.SqlManager.OrmData.DataManager import DataManager


class DeliveryOrder(Base):
    __tablename__ = 'DeliveryOrder'

    id = Column(String(20), primary_key=True)
    plannedDeliveryTime = Column(Date())
    actualDeliveryTime = Column(Date())
    salesOrderId = Column(String(10), ForeignKey('SalesOrder.id'))
    warehouse = Column(String(10), ForeignKey('Warehouse.id'))
    deliveryPhase = Column(Enum('1', '2', '3', '4', '5'))

    def __init__(self, **data):
        self.plannedDeliveryTime = data['plannedDeliveryTime'],
        self.actualDeliveryTime = data['actualDeliveryTime'],
        self.salesOrderId = data['salesOrderId'],
        self.warehouse = data['warehouse'],
        self.deliveryPhase = data['deliveryPhase']

    def __repr__(self):
        return '我还没写'


class DeliveryItem(Base):
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


class DeliveryDataManager(DataManager):
    def __init__(self, session, idrecord, logging):
        '''
        :param session:
        :param idrecord:
        :param logging:
        '''
        super().__init__(session, idrecord, logging)
        self.session = session
        self.logging = logging

    def insertDeliveryOrder(self, data):
        '''

        :param data:
        :return:
        '''
        newData = DeliveryOrder(**data)
        self.insetData(newData)

    def insertDeliveryItem(self, data):
        '''

        :param data:
        :return:
        '''
        newData = DeliveryItem(**data)
        self.insetData(newData)

