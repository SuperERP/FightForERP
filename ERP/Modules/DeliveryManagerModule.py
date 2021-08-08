from .AbstractModule import *
from .OrmData.DeliveryData import *


class DeliveryManagerModule(AbstractModule):
    def __init__(self, session, logging):
        '''
        :param session:
        :param idrecord:
        :param logging:
        '''
        super().__init__(session, logging)

    def deliveryOrder2to3(self, deliveryOrderId, datestr):
        '''
        将发货单的状态从2改为3

        '''
        from dateutil import parser
        try:
            self.session.query(DeliveryOrder).filter(DeliveryOrder.id == deliveryOrderId).update(
                {
                    'deliveryPhase': 3,
                    'actualDeliveryTime': parser.parse(datestr)
                }
            )
            self.session.commit()
        except Exception as e:
            self.logging.info('请重新检查数据插入')
            self.logging.error(e)
            return
        self.logging.info('发货单从状态2转到状态3')
        return

    def deliveryOrder1to2(self):
        '''
        将所有状态处于1的发货单的状态转为状态2
        '''
        info = 0

        try:
            data = self.session.query(DeliveryOrder).all()
            for item in data:
                deliveryItemData = self.session.query(DeliveryItem).filter(
                    DeliveryItem.deliveryOrderId == item.id).all()

                cnt = 0
                for deliveryItem in deliveryItemData:
                    if deliveryItem.pickingStatus == 1:
                        cnt += 1

                if cnt == len(deliveryItemData) and cnt != 0:
                    self.session.query(DeliveryOrder).filter(
                        DeliveryOrder.id == item.id).filter(DeliveryOrder.deliveryPhase == 1).update(
                        {'deliveryPhase': 2})

            self.session.commit()

        except Exception as e:
            self.logging.error(e)
            return
        self.logging.info('完成%r个订单从状态一到状态二的更新工作' % info)

    def pickingDeliveryItems(self, deliveryOrderId=None, materialId=None):
        '''
        完成发货单物料项的拣配工作
        '''
        try:
            self.session.query(DeliveryItem).filter(and_(
                DeliveryItem.deliveryOrderId == deliveryOrderId, DeliveryItem.materialId == materialId)). \
                update({'pickingStatus': 1})
            self.session.commit()
        except Exception as e:
            self.logging.info('请重新检查数据插入')
            self.logging.error(e)
            return
        self.logging.info('发生拣配工作')
        self.deliveryOrder1to2()
        return

    def searchDeliveryItems(self, deliveryId):
        '''
        查询所有的销售订单物料项
        '''
        ret = []
        try:
            for item in self.session.query(DeliveryItem).filter(DeliveryItem.deliveryOrderId == deliveryId).all():
                ret.append(self.to_dict(item))
        except Exception as e:
            self.logging.info('请重新检查数据插入')
            self.logging.error(e)
            return
        self.logging.info('查询所有物料项%r', ret)

        return ret

    def searchallDelivery(self):
        res = []
        for item in self.session.query(DeliveryOrder).all():
            res.append(self.to_dict(item))
        return res

    def insertDeliveryOrder(self, data):
        '''

        :param data:
        :return:返回发货单的Id
        '''

        data['id'] = 'OD' + self.getTimeId()
        newData = DeliveryOrder(**data)
        self.insertData(newData)
        return data['id']

    def insertDeliveryItem(self, data):
        '''

        :param data:
        :return:
        '''
        newData = DeliveryItem(**data)
        self.insertData(newData)

    def getDeliveryOrder(self, id=None):
        res = self.session.query(DeliveryOrder).filter(
            DeliveryOrder.id == id).all()[0]
        return self.to_dict(res)

    def getDeliveryItem(self, deliveryOrderId, materialId):
        return self.to_dict(self.session.query(DeliveryItem).filter(and_(DeliveryItem.materialId == materialId, DeliveryItem.deliveryOrderId == deliveryOrderId)).all()[0])
