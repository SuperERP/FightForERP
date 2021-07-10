from sqlalchemy import *

# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
engine = create_engine('sqlite:///tutorial.db', echo=True)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

# engine = create_engine(DB_URI)
Base = declarative_base(engine)  # SQLORM基类
session = sessionmaker(engine)()  # 构建session对象


class MaterialDic(Base):
    __tablename__ = 'MaterialDic'
    id = Column(String(10), primary_key=True)
    name = Column(Text())
    price = Column(Float())


class Warehouse(Base):
    __tablename__ = 'Warehouse'
    id = Column(String(10), primary_key=True)
    name = Column(String(50))


class Inventory(Base):
    __tablename__ = 'Inventory'
    warehouseId = Column(String(10), ForeignKey('Warehouse.id'))
    materialDicId = Column(String(10), ForeignKey('MaterialDic.id'))
    volume = Column(Float())
    requestVolume = Column(Float())
    onOrderStock = Column(Float())
    __table_args__ = (
        PrimaryKeyConstraint('warehouseId', 'materialDicId'),
    )


class RelationshipDic(Base):
    __tablename__ = 'RelationshipDic'
    relationType = Column(String(10), primary_key=True)
    definition = Column(Text())


class CustomerInformation(Base):
    __tablename__ = 'CustomerInformation'
    id = Column(String(10), primary_key=True)
    name = Column(String(50), nullable=false)
    street = Column(String(50), nullable=false)
    postcode = Column(String(10), nullable=false)
    Country = Column(String(10), nullable=false)
    language = Column(String(10), nullable=false)
    accountantId = Column(String(10), nullable=false)
    paycode = Column(String(10), nullable=false)
    distribution_channel = Column(String(100), nullable=false)
    distribution_area = Column(String(50), nullable=false)
    Tcl = Column(String(10), nullable=false)
    POcode = Column(String(10))


class ContactPerson(Base):
    __tablename__ = 'ContactPersonInformation'
    id = Column(String(10), primary_key=True, nullable=false)
    PrefixName = Column(String(10), nullable=false)
    first_name = Column(String(10))
    last_name = Column(String(10))
    language = Column(String(10))
    country = Column(String(10), nullable=false)
    area = Column(String(10), nullable=false)
    POcode = Column(String(10))


class CustomerAndContactPersonRelationship(Base):
    __tablename__ = 'CustomerAndContactPerson'
    customerId = Column(String(10), ForeignKey('CustomerInformation.id'))
    contactId = Column(String(10), ForeignKey('ContactPersonInformation.id'))
    relationType = Column(String(10), ForeignKey('RelationshipDic.relationType'))
    POcode = Column(String(10))
    __table_args__ = (
        PrimaryKeyConstraint('customerId', 'contactId', 'relationType'),
    )


class Inquiry(Base):
    __tablename__ = 'Inquiry'
    id = Column(String(10), primary_key=True)
    POcode = Column(String(10))
    PODate = Column(Date())
    effectiveDate = Column(Date())
    invalidDate = Column(Date())


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


class Discount(Base):
    '''
    折扣词条
    '''
    __tablename__ = 'Discount'
    id = Column(String(10), primary_key=True)
    name = Column(Text())
    DisCalcu = Column(Text())


class Quotation(Base):
    __tablename__ = 'Quotation'
    id = Column(String(10), primary_key=True)
    # 客户编号
    CustomerId = Column(String(10), ForeignKey('CustomerInformation.id'))
    warehouseId = Column(String(), ForeignKey('Warehouse.id'))
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


class QuotationItem(Base):
    __tablename__ = 'Quotationitem'
    quotationId = Column(String(10), ForeignKey('Quotation.id'))
    materialId = Column(String(10), ForeignKey('MaterialDic.id'))
    description = Column(Text())
    # 数量
    amount = Column(Integer())
    unit = Column(String(10))
    disId = Column(String(10), ForeignKey('Discount.id'))
    disAmount = Column(String())
    __table_args__ = (
        # 联合主键约束
        PrimaryKeyConstraint('quotationId', 'materialId'),
    )


class SalesOrder(Base):
    '''
    销售订单
    '''
    __tablename__ = 'Salesorder'
    id = Column(String(10), primary_key=True)

    customerId = Column(String(10), ForeignKey('CustomerInformation.id'))
    warehouse = Column(String(10), ForeignKey('Warehouse.id'))
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


class Invoice(Base):
    __tablename__ = 'Invoice'
    id = Column(String(10), primary_key=True)
    plannedDeliveryTime = Column(Date())
    actualDeliveryTime = Column(Date())
    salesOrderId = Column(String(10), ForeignKey('Salesorder.id'))
    warehouse = Column(String(10), ForeignKey('Warehouse.id'))
    deliveryPhase = Column(Enum('1', '2', '3', '4', '5'))


class InvoiceItem(Base):
    __tablename__ = 'InvoiceItem'
    invoiceId = Column(String(10), ForeignKey('Invoice.id'))
    materialId = Column(String(10), ForeignKey('MaterialDic.id'))
    description = Column(Text())
    amount = Column(Integer())
    unit = Column(String(10))
    pickingstatus = Column(Enum(''))
    pickingAmount = Column(Integer())
    materialState = Column(Enum(''))
    __table_args__ = (
        PrimaryKeyConstraint('invoiceId', 'materialId'),
    )


Base.metadata.create_all()  # 将模型映射到数据库中
data = {'id': 'fuck', 'name': 'fasd', ' price': 'adsf'}
session.add_all([
    MaterialDic(id='fuck', name='das', price=19.0)

])

session.commit()
