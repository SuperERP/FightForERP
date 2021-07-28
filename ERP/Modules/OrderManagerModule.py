from .AbstractModule import AbstractModule
from .OrmData.QutationAndSalesOrderData import *
from .OrmData.InquiryData import *
from ERP.Modules.OrmData.WareHouse import Warehouse


class OrderManagerModule(AbstractModule):
    def __init__(self, session, logging):
        '''
        :param session:
        :param idrecord:
        :param logging:
        '''
        super().__init__(session, logging)
        
    def insertInquiry(self, data: dict):
        '''
        向数据库中插入询价单
        :param data:
        :return:
        '''
        Base.metadata.create_all()
        data['id'] = 'IN' + self.getTimeId()
        newData = Inquiry(**data)
        self.insertData(newData)
        return(data['id'])

    def insertInquiryItem(self, data: dict):
        '''
        向数据库中插入询价单物料项
        :param data:
        :return:
        '''
        newData = InquiryItem(**data)
        self.insertData(newData)

    def insertQuotation(self, data: dict):
        '''
        向数据库中插入报价单
        :param data:
        :return:
        '''
        Base.metadata.create_all()
        data['id'] = 'QU' + self.getTimeId()
        newData = Quotation(**data)
        self.insertData(newData)
        return(data['id'])

    def insertQuotationItem(self, data: dict):
        '''
        向数据库中插入报价单物料项
        :param data:
        :return:
        '''
        newData = QuotationItem(**data)
        self.insertData(newData)

    def searchOrders(self, customerId=None, warehouseId=None, saleorderId=None):

        def getSaleOrders(data):
            print(data)

            id = data['warehouseId']
            self.logging.info(id)
            data['warehousename'] = self.session.query(
                Warehouse).filter(Warehouse.id == id).all()[0].name
            return data

        ret=[]
        if saleorderId is not None:
            for idata in self.session.query(SalesOrder).filter(SalesOrder.id == saleorderId).all():
                ret.append(getSaleOrders(self.to_dict(idata)))
        else:
            for idata in self.session.query(SalesOrder).all():
                ret.append(getSaleOrders(self.to_dict(idata)))


        return ret

    def insertDiscount(self, data: dict):
        '''
        向数据库中插入折扣
        :param data:
        :return:
        '''
        newData = DiscountDic(**data)
        self.insertData(newData)

    def searchallDiscountDic(self): 
        '''
        查找所有折扣字典
        '''
        res = []
        for item in self.session.query(DiscountDic).all():
            res.append(self.to_dict(item))
        return res

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
