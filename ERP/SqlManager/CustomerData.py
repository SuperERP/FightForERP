from BaseUtil import *


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
    country = Column(String(10), nullable=false)
    language = Column(String(10), nullable=false)
    accountantId = Column(String(10), nullable=false)
    paycode = Column(String(10), nullable=false)
    distribution_channel = Column(String(100), nullable=false)
    distribution_area = Column(String(50), nullable=false)
    # 销售渠道编号
    sales_channel_number = Column(String(10), nullable=false)
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
