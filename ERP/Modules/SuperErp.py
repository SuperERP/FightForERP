from .CustomerManageModule import *
from .OrderManagerModule import *
from .DeliveryManagerModule import *
from .OrmData.WareHouse import *
from .WarehouseManager import *
from .UesrManageModule import *

class SuperErp:
    '''
    真正的erp系统
    '''

    def __init__(self, CustomerManageModule, DeliveryManagerModule, OrderManagerModule):
        self.CustomerManageModule = CustomerManageModule
        self.DeliveryManagerModule = DeliveryManagerModule
        self.OrderManagerModule = OrderManagerModule

    def creatInqury(self, data: dict):
        '''
        创建询价单
        :param data:
        :return:
        '''



        pass



    def createSalesOrder(self, data: dict):
        '''

        :param data:这里的data必须包含有物料编号
        {

        }

        :return:
        '''
        # testData=

        self.OrderManagerModule.createSalesOrder()

        pass
