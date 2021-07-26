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
    name = Column(String(50))
    street = Column(String(50), nullable=false)
    postcode = Column(String(10), nullable=false)
    country = Column(String(10), nullable=false)
    language = Column(String(10), nullable=false)
    city = Column(String(50), nullable=false)
    region = Column(String(50))
    distribution_channel = Column(String(100), nullable=false)
    # distribution_area = Column(String(50), nullable=false)
    # 销售渠道编号
    sales_channel_number = Column(String(10), nullable=false)
    POcode = Column(String(10))

    def __init__(self, **data):
        self.id = data['id']
        self.name = data['name']
        self.street = data['street']
        self.postcode = data['postcode']
        self.country = data['country']
        self.language = data['language']
        self.city = data['city']
        self.distribution_channel = data['distribution_channel']
        self.region = data['region']
        self.sales_channel_number = data['sales_channel_number']
        self.POcode = data['POcode']

    def __repr__(self):
        return '<Customer(id=%r,name=%r, street=%r,postcode=%r,country=%r,language=%r,paycode=%r,' \
               'distribution_channel=%r,city=%r,sregion=%r,POcode=%r)>' % (
                   self.id, self.name,
                   self.street, self.postcode,
                   self.country, self.language,self.city,
                   self.distribution_channel, self.city,
                   self.region, self.POcode
               )


class ContactPerson(Base):
    __tablename__ = 'ContactPerson'
    id = Column(String(30), primary_key=True, nullable=false)
    prefixName = Column(String(10), nullable=false)
    first_name = Column(String(10), nullable=false)
    last_name = Column(String(10), nullable=false)
    language = Column(String(10))
    country = Column(String(10))
    # area = Column(String(10), nullable=false)
    POcode = Column(String(10))

    def __init__(self, **data):
        self.id = data['id']
        self.prefixName = data['prefixName']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.language = data['language']
        self.country = data['country']
        # self.area = data['area']
        self.POcode = data['POcode']

    def __repr__(self):
        return '<ContactPerson(id=%r, prefixName=%r,first_name=%r,last_name=%r,language=%r,country=%r,POcode=%r' \
               % \
               (
                   self.id, self.prefixName, self.first_name, self.last_name, self.language, self.country,self.POcode
               )


class CustomerAndContactPersonRelationship(Base):
    __tablename__ = 'CustomerAndContactPerson'

    id = Column(String(30), primary_key=True) 
    customerId = Column(String(20), ForeignKey('Customer.id'))
    contactId = Column(String(20), ForeignKey('ContactPerson.id'))
    relationType = Column(String(10), ForeignKey('RelationshipDic.relationType'))
    validTo = Column(Date())
    validFrom = Column(Date())
    POcode = Column(String(10))

    # __table_args__ = (
    #     PrimaryKeyConstraint('customerId', 'contactId', 'relationType'),
    # )

    def __init__(self, **data):
        self.id = data['id']
        self.customerId = data['customerId']
        self.contactId = data['contactId']
        self.relationType = data['relationType']
        self.validFrom = data['validFrom']
        self.validTo = data['validTo']
        self.POcode = data['Pocode']

    def __repr__(self):
        return '<CustomerAndContactPerson(customerId=%r,)>'
