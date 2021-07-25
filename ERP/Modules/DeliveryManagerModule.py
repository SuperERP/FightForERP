from .AbstractModule import *
from .OrmData.DeliveryData import *


class DeliveryManagerModule(AbstractModule):
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
        self.insertData(newData)

    def insertDeliveryItem(self, data):
        '''

        :param data:
        :return:
        '''
        newData = DeliveryItem(**data)
        self.insertData(newData)
