from ERP.SqlManager.BaseUtil import *



class Inquiry(Base):
    __tablename__ = 'Inquiry'
    id = Column(String(20), primary_key=True)
    POcode = Column(String(10))
    PODate = Column(Date())
    effectiveDate = Column(Date())
    expirationDate = Column(Date())

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.POcode = kwargs['POcode']
        self.PODate = kwargs['PODate']
        self.effectiveDate = kwargs['effectiveDate']
        self.expirationDate = kwargs['expirationDate']

    def __repr__(self):
        return '<Inquiry(id=%r,POcode=%r,PODate=%r,effectiveDate=%r,expirationDate=%r)>' % (
            self.id, self.POcode, self.PODate, self.effectiveDate, self.expirationDate
        )


class InquiryItem(Base):
    '''
    询价单物料项
    '''
    __tablename__ = 'InquiryItem'
    # 询价单编号
    inquiryId = Column(String(20), ForeignKey('Inquiry.id'))
    # 报价单编号
    materialId = Column(String(10), ForeignKey('MaterialDic.id'))

    descpription = Column(Text())
    count = Column(Integer())
    unit = Column(String(10))
    probability = Column(Float())
    __table_args__ = (
        # 联合主键约束
        PrimaryKeyConstraint('inquiryId', 'materialId'),
    )

    def __init__(self, **kwargs):
        self.inquiryId = kwargs['inquiryId']
        self.materialId = kwargs['materialId']
        self.descpription = kwargs['descpription']
        self.count = kwargs['count']
        self.unit = kwargs['unit']
        self.probability = kwargs['probability']

    def __repr__(self):
        return '<InquiryItem(inquiryId=%r,materialId=%r,descpription=%r,count=%r,unit=%r,probability=%r)>' % (
            self.inquiryId, self.materialId, self.descpription, self.count, self.unit, self.probability
        )
