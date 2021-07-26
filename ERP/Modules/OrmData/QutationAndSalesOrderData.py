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
    cnty = Column(String(10), ForeignKey('DiscountDic.id'))
    ## 总体折扣数量
    totalCntyPercent = Column(Integer())

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
        self.cnty = Column(String(10), ForeignKey('DiscountDic.id'))
        ## 总体折扣数量
        self.totalCntyPercent = Column(Integer())


class QuotationItem(Base):
    __tablename__ = 'Quotationitem'

    quotationId = Column(String(30), ForeignKey('Quotation.id'))
    material = Column(String(10), ForeignKey('MaterialDic.id'))
    itemDescription = Column(Text())
    orderQuantity = Column(Integer())
    salesUnit = Column(String(10))
    cnty = Column(String(10), ForeignKey('DiscountDic.id'))
    amount = Column(Integer()) #折扣数量命名
    __table_args__ = (
        # 联合主键约束
        PrimaryKeyConstraint('quotationId', 'material'),
    )

    def __init__(self, **kwargs):
        self.quotationId = kwargs['quotationId']
        self.material = kwargs['material']
        self.itemDescription = kwargs['itemDescription']
        self.orderQuantity = kwargs['orderQuantity']
        self.salesUnit = kwargs['salesUnit']
        self.cnty = kwargs['cnty']
        self.amount = kwargs['amount']


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
    orderQuantity = Column(Integer())
    salesUnit = Column(String(10))
    cnty = Column(String(10), ForeignKey('DiscountDic.id'))
    amount = Column(Integer())

    __table_args__ = (
        # 联合主键约束
        PrimaryKeyConstraint('saleOrderId', 'material'),
    )

    def __init__(self, **kwargs):
        self.saleOrderId = kwargs['saleOrderId']
        self.material = kwargs['material']
        self.itemDescription = kwargs['itemDescription']
        self.orderQuantity = kwargs['orderQuantity']
        self.salesUnit = kwargs['salesUnit']
        self.cnty = kwargs['cnty']
        self.amount = kwargs['amount']
