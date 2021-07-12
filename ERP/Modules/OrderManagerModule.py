from .AbstractModule import AbstractModule
from .OrmData.QutationAndSalesOrderData import *
from .OrmData.InquiryData import *


class OrderManagerModule(AbstractModule):
    def __init__(self, session, logging):
        '''
        :param session:
        :param idrecord:
        :param logging:
        '''
        super().__init__(session, logging)
        self.logging = logging

    def insertDiscount(self, data: dict):
        '''
        向数据库中插入折扣
        :param data:
        :return:
        '''
        newData = Discount(**data)
        self.insetData(newData)

    def createSalesOrder(self, data):
        '''
        创建销售订单的时候创建发货单
        :param data:
        :return:生成的销售订单的编号

        '''
        # 生成销售订单的编号
        testdata = {
            'customerId': 'dfsaf',
            'warehouse': '2011-05-06',
            'POcode': '050',
            'PODate': '2011-05-06',
            'effectiveDate': '2011-05-06',
            'expirationDate': '2011-05-06',
            'requestedDeliveryDate': '2011-05-06',
            'discountId': 'zk101',
            'totalDiscountNum': '',
            'materialList': ['sb101', 'sb102', 'sb103', 'sb104']
        }

        data['id'] = 'SO' + self.getTimeId()

        newSalesOrder = SalesOrder(**data)

        return data['id']
