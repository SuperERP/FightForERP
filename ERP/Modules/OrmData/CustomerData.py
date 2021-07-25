from .BaseUtil import *


class RelationshipDic(Base):
    '''
    写死的
    '''
    __tablename__ = 'RelationshipDic'
    relationType = Column(String(10), primary_key=True)
    definition = Column(Text())

    def __init__(self, **kwargs):
        self.relationType = kwargs['relationType']
        self.definition = kwargs['definition']

    def __repr__(self):
        return '<RelationshipDic(relationType=%r, definition=%r)>' % (self.relationType, self.definition)


class Customer(Base):
    __tablename__ = 'Customer'

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

    def __init__(self, **data):
        self.id = data['id']
        self.name = data['name'],
        self.street = data['street'],
        self.postcode = data['postcode'],
        self.country = data['country'],
        self.language = data['language'],
        self.accountantId = data['accountantId'],
        self.paycode = data['paycode'],
        self.distribution_channel = data['distribution_channel'],
        self.distribution_area = data['distribution_area'],
        self.sales_channel_number = data['sales_channel_number'],
        self.POcode = data['POcdoe']

    def __repr__(self):
        return '<Customer(id=%r,name=%r, street=%r,postcode=%r,country=%r,language=%r,accountantId=%r,paycode=%r,' \
               'distribution_channel=%r,distribution_area=%r,sales_channel_number=%r,POcode=%r)>' % (
                   self.id, self.name,
                   self.street, self.postcode,
                   self.country, self.language,
                   self.accountantId, self.paycode,
                   self.distribution_channel, self.distribution_area,
                   self.sales_channel_number, self.POcode
               )


class ContactPerson(Base):
    __tablename__ = 'ContactPerson'
    id = Column(String(20), primary_key=True, nullable=false)
    prefixName = Column(String(10), nullable=false)
    first_name = Column(String(10))
    last_name = Column(String(10))
    language = Column(String(10))
    country = Column(String(10), nullable=false)
    area = Column(String(10), nullable=false)
    POcode = Column(String(10))

    def __init__(self, **data):
        self.id = data['name']
        self.name = data['name'],
        self.prefixName = data['prefixName'],
        self.first_name = data['first_name'],
        self.second_name = data['second_name'],
        self.language = data['language'],
        self.country = data['country'],
        self.area = data['area'],
        self.POcode = data['POcode']

    def __repr__(self):
        return '我还没写'


class CustomerAndContactPersonRelationship(Base):
    __tablename__ = 'CustomerAndContactPerson'

    customerId = Column(String(20), ForeignKey('Customer.id'))
    contactId = Column(String(20), ForeignKey('ContactPerson.id'))
    relationType = Column(String(10), ForeignKey('RelationshipDic.relationType'))
    POcode = Column(String(10))

    __table_args__ = (
        PrimaryKeyConstraint('customerId', 'contactId', 'relationType'),
    )

    def __init__(self, **data):
        self.customerId = data['customerId'],
        self.contactId = data['contactId'],
        self.relationType = data['relationType'],
        self.POcode = data['Pocode']

    def __repr__(self):
        return '我还没写'
