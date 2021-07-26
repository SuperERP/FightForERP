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

    def searchallDelivery(self):
        res = []
        for item in self.session.query(DeliveryOrder).all():
            res.append(self.to_dict(item))
        return res

    def insertDeliveryOrder(self, data):
        '''

        :param data:
        :return:
        '''

        data['id'] = 'OD' + self.getTimeId()
        newData = DeliveryOrder(**data)
        self.insertData(newData)

    def insertDeliveryItem(self, data):
        '''

        :param data:
        :return:
        '''
        newData = DeliveryItem(**data)
        self.insertData(newData)
