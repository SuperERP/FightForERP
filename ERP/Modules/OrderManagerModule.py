from .AbstractModule import AbstractModule
from .OrmData.QutationAndSalesOrderData import *
from .OrmData.InquiryData import *
from ERP.Modules.OrmData.WareHouse import MaterialDic, Warehouse


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
        :return:询价单号
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
        :return:报价单号
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
        创建销售订单的，同时创建发货单
        :param data:
        :return:生成的销售订单的编号

        '''
        # 生成销售订单的编号

        data['id'] = 'SO' + self.getTimeId()

        newSalesOrder = SalesOrder(**data)
        self.insertData(newSalesOrder)
        return data['id']

    def insertSalesOrderItem(self, data: dict):
        '''
        向数据库中插入销售订单物料项
        :param data:
        :return:
        '''
        Base.metadata.create_all()
        newData = SalesOrderItem(**data)
        self.insertData(newData)

    def searchInquiry(self, id='',customerId='',warehouseId='',POcode='',PODate='',effectiveDate='',expirationDate=''):
        '''
        按条件查找询价单
        '''
        res=[]

        for idata in self.session.query(Inquiry).filter(or_(Inquiry.id==id,id==''))\
            .filter(or_(Inquiry.customerId==customerId,customerId==''))\
                .filter(or_(Inquiry.warehouseId==warehouseId,warehouseId==''))\
                    .filter(or_(Inquiry.POcode==POcode,POcode==''))\
                        .filter(or_(Inquiry.PODate==PODate,PODate==''))\
                            .filter(or_(Inquiry.effectiveDate==effectiveDate,effectiveDate==''))\
                                .filter(or_(Inquiry.expirationDate==expirationDate,expirationDate=='')).all():
            res.append(self.to_dict(idata))

        return res

    def searchInquiryItem(self, inquiryId):
        '''
        根据给定询价单号查找询价单物料项，并加入price
        '''
        res=[]

        for idata in self.session.query(InquiryItem).filter(InquiryItem.inquiryId == inquiryId).all():
            a = self.to_dict(idata)
            a['price'] = self.to_dict(self.session.query(MaterialDic).filter(MaterialDic.id == a['material']).all()[0])['price']
            res.append(a)

        return res
    
    def searchQuotation(self, id='',customerId='',warehouseId='',POcode='',PODate='',effectiveDate='',expirationDate='',requestedDeliveryDate=''):
        '''
        按条件查找报价单
        '''
        res=[]

        for idata in self.session.query(Quotation).filter(or_(Quotation.id==id,id==''))\
            .filter(or_(Quotation.customerId==customerId,customerId==''))\
                .filter(or_(Quotation.warehouseId==warehouseId,warehouseId==''))\
                    .filter(or_(Quotation.POcode==POcode,POcode==''))\
                        .filter(or_(Quotation.PODate==PODate,PODate==''))\
                            .filter(or_(Quotation.effectiveDate==effectiveDate,effectiveDate==''))\
                                .filter(or_(Quotation.requestedDeliveryDate==requestedDeliveryDate,requestedDeliveryDate==''))\
                                    .filter(or_(Quotation.expirationDate==expirationDate,expirationDate=='')).all():
            res.append(self.to_dict(idata))

        return res
    
    def searchQuotationItem(self, quotationId):
        '''
        根据给定报价单号查找报价单物料项，并加入price
        '''
        res=[]

        for idata in self.session.query(QuotationItem).filter(QuotationItem.quotationId == quotationId).all():
            a = self.to_dict(idata)
            a['price'] = self.to_dict(self.session.query(MaterialDic).filter(MaterialDic.id == a['material']).all()[0])['price']
            res.append(a)

        return res
    
    def searchSalesOrder(self, id='',customerId='',warehouseId='',POcode='',PODate='',effectiveDate='',expirationDate=''):
        '''
        按条件查找销售订单
        '''
        res=[]

        for idata in self.session.query(SalesOrder).filter(or_(SalesOrder.id==id,id==''))\
            .filter(or_(SalesOrder.customerId==customerId,customerId==''))\
                .filter(or_(SalesOrder.warehouseId==warehouseId,warehouseId==''))\
                    .filter(or_(SalesOrder.POcode==POcode,POcode==''))\
                        .filter(or_(SalesOrder.PODate==PODate,PODate==''))\
                            .filter(or_(SalesOrder.effectiveDate==effectiveDate,effectiveDate==''))\
                                .filter(or_(SalesOrder.expirationDate==expirationDate,expirationDate=='')).all():
            res.append(self.to_dict(idata))

        return res
    
    def searchSalesOrderItem(self, salesOrderId):
        '''
        根据给定销售订单号查找销售订单物料项，并加入price
        '''
        res=[]

        for idata in self.session.query(SalesOrderItem).filter(SalesOrderItem.salesOrderId == salesOrderId).all():
            a = self.to_dict(idata)
            a['price'] = self.to_dict(self.session.query(MaterialDic).filter(MaterialDic.id == a['material']).all()[0])['price']
            res.append(a)

        return res

    def changeInquiry(self,id, data :dict):
        '''
        修改询价单，并清空该询价单下的物料项
        '''
        try:
            self.session.query(Inquiry).filter(Inquiry.id==id).update(data)
            self.session.query(InquiryItem).filter(InquiryItem.inquiryId == id).delete()
            self.session.commit()
        except Exception as e:
            self.logging.info('请重新检查数据修改')
            self.logging.error(e)
            self.session.rollback()

    def changeQuotation(self,id, data :dict):
        '''
        修改报价单，并清空该报价单下的物料项
        '''
        try:
            self.session.query(Quotation).filter(Quotation.id==id).update(data)
            self.session.query(QuotationItem).filter(QuotationItem.quotationId == id).delete()
            self.session.commit()
        except Exception as e:
            self.logging.info('请重新检查数据修改')
            self.logging.error(e)
            self.session.rollback()
    
    def changeSalesOrder(self,id, data :dict):
        '''
        修改销售订单，并清空该销售订单下的物料项
        '''
        try:
            self.session.query(SalesOrder).filter(SalesOrder.id==id).update(data)
            self.session.query(SalesOrderItem).filter(SalesOrderItem.salesOrderId == id).delete()
            self.session.commit()
        except Exception as e:
            self.logging.info('请重新检查数据修改')
            self.logging.error(e)
            self.session.rollback()