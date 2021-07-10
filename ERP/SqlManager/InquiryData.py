from BaseUtil import *


class Inquiry(Base):
    __tablename__ = 'Inquiry'
    id = Column(String(10), primary_key=True)
    POcode = Column(String(10))
    PODate = Column(Date())
    effectiveDate = Column(Date())
    expirationDate = Column(Date())


class InquiryItem(Base):
    '''
    询价单物料项
    '''
    __tablename__ = 'InquiryItem'
    # 询价单编号
    inquiryId = Column(String(10), ForeignKey('Inquiry.id'))
    # 报价单编号
    materialId = Column(String(10), ForeignKey('MaterialDic.id'))
    __table_args__ = (
        # 联合主键约束
        PrimaryKeyConstraint('inquiryId', 'materialId'),
    )
    descpription = Column(Text())
    count = Column(Integer())
    unit = Column(String(10))
    probability = Column(Float())
