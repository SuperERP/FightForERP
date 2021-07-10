from BaseUtil import *


class DeliveryOrder(Base):
    __tablename__ = 'DeliveryOrder'
    id = Column(String(10), primary_key=True)
    plannedDeliveryTime = Column(Date())
    actualDeliveryTime = Column(Date())
    salesOrderId = Column(String(10), ForeignKey('SalesOrder.id'))
    warehouse = Column(String(10), ForeignKey('Warehouse.id'))
    deliveryPhase = Column(Enum('1', '2', '3', '4', '5'))


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


class DeliveryDataManager:
    def __init__(self, session, idrecord, logging):
        '''
        :param session:
        :param idrecord:
        :param logging:
        '''
        self.session = session
        self.logging = logging
        pass

    def createDeliveryItem(self, data):
        '''

        :param data:
        :return:
        '''
        newDeliveryItem = DeliveryItem(
            deliveryOrderId=data['deliveryOrderId'],
            materialId=data['materialId'],
            description=data['description'],
            amount=data['amount'],
            unit=data['unit'],
            pickingStatus=data['pickingStatus'],
            pickingAmount=data['pickingAmount'],
            materialState=data['materialState']
        )
        return newDeliveryItem

    def createDeliveryOrder(self, data):
        '''
        创建DelieryOrder ORM对象
        :param data:
        :return:
        '''
        newDelieryOrder = DeliveryOrder(
            plannedDeliveryTime=data['plannedDeliveryTime'],
            actualDeliveryTime=data['actualDeliveryTime'],
            salesOrderId=data['salesOrderId'],
            warehouse=data['warehouse'],
            deliveryPhase=data['deliveryPhase']
        )
        return newDelieryOrder

    def insertDeliveryOrder(self, data):
        '''

        :param data:
        :return:
        '''
        newData = self.createDeliveryOrder(data)
        try:
            self.session.add(newData)
        except Exception as e:
            self.logging.error(e)
            self.session.rollback()
        finally:
            self.logging.info('请重新检查数据插入')

    def insertDeliveryItem(self, data):
        '''

        :param data:
        :return:
        '''
        newData = self.createDeliveryItem(data)
        try:
            self.session.add(newData)
            self.logging.info('插入数据%s'%str(data))
        except Exception as e:
            self.logging.error(e)
            self.session.rollback()
        finally:
            self.logging.info('请重新检查数据插入')
