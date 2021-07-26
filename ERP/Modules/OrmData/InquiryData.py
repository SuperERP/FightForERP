from .BaseUtil import *



class Inquiry(Base):
    __tablename__ = 'Inquiry'
    id = Column(String(20), primary_key=True)
    customerId = Column(String(20), ForeignKey('Customer.id'))
    warehouseId = Column(String(10), ForeignKey('Warehouse.id')) 
    POcode = Column(String(10))
    PODate = Column(Date())
    effectiveDate = Column(Date())
    expirationDate = Column(Date())

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.customerId = kwargs['customerId']
        self.warehouseId = kwargs['warehouseId']
        self.POcode = kwargs['POcode']
        self.PODate = kwargs['PODate']
        self.effectiveDate = kwargs['effectiveDate']
        self.expirationDate = kwargs['expirationDate']

    # def __repr__(self):
    #     return '<Inquiry(id=%r,POcode=%r,PODate=%r,effectiveDate=%r,expirationDate=%r)>' % (
    #         self.id, self.POcode, self.PODate, self.effectiveDate, self.expirationDate
    #     )


class InquiryItem(Base):
    '''
    询价单物料项
    '''
    __tablename__ = 'InquiryItem'
    # 询价单编号
    inquiryId = Column(String(20), ForeignKey('Inquiry.id'))
    material = Column(String(10), ForeignKey('MaterialDic.id'))
    itemDescription = Column(Text())
    orderQuantity = Column(Integer())
    salesUnit = Column(String(10))
    orderProbility = Column(Float())
    __table_args__ = (
        # 联合主键约束
        PrimaryKeyConstraint('inquiryId', 'material'),
    )

    def __init__(self, **kwargs):
        self.inquiryId = kwargs['inquiryId']
        self.material = kwargs['material']
        self.itemDescription = kwargs['itemDescription']
        self.orderQuantity = kwargs['orderQuantity']
        self.salesUnit = kwargs['salesUnit']
        self.orderProbility = kwargs['orderProbility']

    def __repr__(self):
        pass
