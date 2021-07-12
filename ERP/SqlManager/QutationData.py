from BaseUtil import *


class Discount(Base):
    '''
    折扣词条
    '''
    __tablename__ = 'Discount'
    id = Column(String(10), primary_key=True)
    name = Column(Text())
    DiscountCalcu = Column(Text())


class Quotation(Base):
    __tablename__ = 'Quotation'
    id = Column(String(10), primary_key=True)
    # 客户编号
    CustomerId = Column(String(10), ForeignKey('Customer.id'))
    warehouseId = Column(String(), ForeignKey('Warehouse.id'))
    POcode = Column(String(10))
    PODate = Column(Date())
    effectiveDate = Column(Date())
    expirationDate = Column(Date())
    # 请求交货日期
    requestedDeliveryDate = Column(Date())
    # 折扣数量
    discountId = Column(String(10), ForeignKey('Discount.id'))
    # 总体折扣数量
    totalDiscountNum = Column(Integer())


class QuotationItem(Base):
    __tablename__ = 'Quotationitem'
    quotationId = Column(String(10), ForeignKey('Quotation.id'))
    materialId = Column(String(10), ForeignKey('MaterialDic.id'))
    description = Column(Text())
    # 数量
    amount = Column(Integer())
    unit = Column(String(10))
    discountId = Column(String(10), ForeignKey('Discount.id'))
    discountAmount = Column(String())
    __table_args__ = (
        # 联合主键约束
        PrimaryKeyConstraint('quotationId', 'materialId'),
    )


class SalesOrder(Base):
    '''
    销售订单
    '''
    __tablename__ = 'SalesOrder'
    id = Column(String(10), primary_key=True)

    customerId = Column(String(10), ForeignKey('Customer.id'))
    warehouseId = Column(String(10), ForeignKey('Warehouse.id'))
    POcode = Column(String(10))
    PODate = Column(Date())

    effectiveDate = Column(Date())

    expirationDate = Column(Date())
    # 请求交货日期
    requestedDeliveryDate = Column(Date())
    # 折扣数量
    discountId = Column(String(10), ForeignKey('Discount.id'))
    # 总体折扣数量
    totalDiscountNum = Column(Integer())


class QutationDataManager:
    def __init__(self, session, idrecord, logging):
        '''
        :param session:
        :param idrecord:
        :param logging:
        '''
        self.session = session
        self.logging = logging

    def createSalesOrder(self, data):

        pass
