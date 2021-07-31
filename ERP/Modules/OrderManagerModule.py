from .AbstractModule import AbstractModule
from .OrmData.QutationAndSalesOrderData import *
from .OrmData.InquiryData import *
from ERP.Modules.OrmData.WareHouse import Warehouse
from .OrmData.CustomerData import *


class OrderManagerModule(AbstractModule):
    def __init__(self, session, logging):
        '''
        :param session:
        :param idrecord:
        :param logging:
        '''
        super().__init__(session, logging)

    def searchAllSalesOrderItems(self, saleOrderId):
        '''
        寻找所有的销售订单物料项
        @return :注意这里返回的是类的列表
        '''
        data = self.session.query(SalesOrderItem).filter(SalesOrderItem.saleOrderId == saleOrderId).all()

        return data

    def searchOrders(self, id='', customerId='', warehouseId='', POcode='', PODate='', effectiveDate='',
                     expirationDate='',
                     saleorderId=None):
        def getSaleOrders(data):
            '''
            获得销售订单关联的warehouse的名字
            客户的名字
            '''
            warehouseid = data['warehouseId']
            data['warehouseName'] = self.session.query(
                Warehouse).filter(Warehouse.id == warehouseid).all()[0].name

            cusId = data['customerId']
            data['customerName'] = self.session.query(Customer).filter(Customer.id == cusId).all()[0].name
            return data

        if saleorderId is not None:
            return getSaleOrders(self.to_dict(self.session.query(SalesOrder).filter(SalesOrder.id == saleorderId).all()[0]))

        res = []

        for idata in self.session.query(SalesOrder).filter(or_(SalesOrder.id == id, id == '')) \
                .filter(or_(SalesOrder.customerId == customerId, customerId == '')) \
                .filter(or_(SalesOrder.warehouseId == warehouseId, warehouseId == '')) \
                .filter(or_(SalesOrder.POcode == POcode, POcode == '')) \
                .filter(or_(SalesOrder.PODate == PODate, PODate == '')) \
                .filter(or_(SalesOrder.effectiveDate == effectiveDate, effectiveDate == '')) \
                .filter(or_(SalesOrder.expirationDate == expirationDate, expirationDate == '')).all():
            res.append(getSaleOrders(self.to_dict(idata)))
        return res

    def insertSalesOrderItem(self, data: dict):
        '''
        向数据库中插入销售订单物料项
        :param data:
        :return:
        '''
        Base.metadata.create_all()
        newData = SalesOrderItem(**data)
        self.insertData(newData)

    def insertDiscount(self, data: dict):
        '''
        向数据库中插入折扣
        :param data:
        :return:
        '''
        newData = DiscountDic(**data)
        self.insertData(newData)

    def createSalesOrder(self, data):
        '''
        创建销售订单的时候创建发货单
        :param data:
        :return:生成的销售订单的编号

        '''
        # 生成销售订单的编号

        data['id'] = 'SO' + self.getTimeId()

        newSalesOrder = SalesOrder(**data)
        self.insertData(newSalesOrder)
        return data['id']
