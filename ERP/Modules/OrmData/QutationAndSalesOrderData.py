from .BaseUtil import *


class DiscountDic(Base):
    '''
    折扣词条
    '''
    __tablename__ = 'DiscountDic'

    id = Column(String(10), primary_key=True)
    name = Column(Text())
    # A代表百分比，B代表固定数值

    discountCalcu = Column(Enum('A', 'B'))

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.discountCalcu = kwargs['discountCalcu']

    def __repr__(self):
        return '<DiscountDic(id=%r,name=%r,discountCalcu=%r)>' % (self.id, self.name, self.discountCalcu)


class Quotation(Base):
    __tablename__ = 'Quotation'
    id = Column(String(20), primary_key=True)
    # 客户编号
    customerId = Column(String(10), ForeignKey('Customer.id'))
    warehouseId = Column(String(10), ForeignKey('Warehouse.id'))
    POcode = Column(String(10))
    PODate = Column(Date())
    effectiveDate = Column(Date())
    expirationDate = Column(Date())
    ## 请求交货日期
    requestedDeliveryDate = Column(Date())
    ## 折扣数量
    discountId = Column(String(10), ForeignKey('Discount.id'))
    ## 总体折扣数量
    totalDiscountNum = Column(Integer())

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        # 客户编号
        self.customerId = kwargs['customerId']
        self.warehouseId = kwargs['warehouseId']
        self.POcode = kwargs['POcode']
        self.PODate = kwargs['PODate']
        self.effectiveDate = Column(Date())
        self.expirationDate = Column(Date())
        ## 请求交货日期
        self.requestedDeliveryDate = Column(Date())
        ## 折扣数量
        self.discountId = Column(String(10), ForeignKey('Discount.id'))
        ## 总体折扣数量
        self.totalDiscountNum = Column(Integer())


class QuotationItem(Base):
    __tablename__ = 'Quotationitem'

    quotationId = Column(String(30), ForeignKey('Quotation.id'))
    materialId = Column(String(10), ForeignKey('MaterialDic.id'))
    description = Column(Text())
    amount = Column(Integer())
    unit = Column(String(10))
    discountId = Column(String(10), ForeignKey('Discount.id'))
    discountAmount = Column(Integer())
    __table_args__ = (
        # 联合主键约束
        PrimaryKeyConstraint('quotationId', 'materialId'),
    )

    def __init__(self, **kwargs):
        self.quotationId = kwargs['quotationId']
        self.materialId = kwargs['materialId']
        self.description = kwargs['description']
        self.amount = kwargs['amount']
        self.unit = kwargs['unit']
        self.discountId = kwargs['discountId']
        self.discountAmount = kwargs['discountAmount']


class SalesOrder(Base):
    '''
    销售订单
    '''
    __tablename__ = 'SalesOrder'
    id = Column(String(30), primary_key=True)

    customerId = Column(String(20), ForeignKey('Customer.id'))
    warehouseId = Column(String(10), ForeignKey('Warehouse.id'))
    POcode = Column(String(10))
    PODate = Column(Date())

    effectiveDate = Column(Date())

    expirationDate = Column(Date())
    requestedDeliveryDate = Column(Date())
    cnty = Column(String(10), ForeignKey('DiscountDic.id'))
    totalCntyPercent = Column(Integer())

    def __init__(self, **data):
        self.id = data['id']
        self.customerId = data['customerId']
        self.warehouseId = data['warehouseId']
        self.POcode = data['POcode']
        self.PODate = data['PODate']
        self.effectiveDate = data['effectiveDate']
        self.expirationDate = data['expirationDate']
        self.requestedDeliveryDate = data['requestedDeliveryDate']
        self.cnty = data['cnty']
        self.totalCntyPercent = data['totalCntyPercent']

    def __repr__(self):
        return '<>'


class SalesOrderItem(Base):
    __tablename__ = 'SalesOrderItem'
    saleOrderId = Column(String(30), ForeignKey('SalesOrder.id'))
    material = Column(String(10), ForeignKey('MaterialDic.id'))
    itemDescription = Column(Text())
    amount = Column(Integer())
    discountId = Column(String(10), ForeignKey('DiscountDic.id'))
    totalDiscountNum = Column(Integer())

    __table_args__ = (
        # 联合主键约束
        PrimaryKeyConstraint('saleOrderId', 'material'),
    )

    def __init__(self, **kwargs):
        pass
