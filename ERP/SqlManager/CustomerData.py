from BaseUtil import *


class RelationshipDic(Base):
    __tablename__ = 'RelationshipDic'
    relationType = Column(String(10), primary_key=True)
    definition = Column(Text())

    def __repr__(self):
        return "<BookOwner(uid='%s', bid='%s', name='%s')>" % (self.uid, self.bid, self.name)


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


class ContactPerson(Base):
    __tablename__ = 'ContactPerson'
    id = Column(String(10), primary_key=True, nullable=false)
    prefixName = Column(String(10), nullable=false)
    first_name = Column(String(10))
    last_name = Column(String(10))
    language = Column(String(10))
    country = Column(String(10), nullable=false)
    area = Column(String(10), nullable=false)
    POcode = Column(String(10))


class CustomerAndContactPersonRelationship(Base):
    __tablename__ = 'CustomerAndContactPerson'
    customerId = Column(String(10), ForeignKey('Customer.id'))
    contactId = Column(String(10), ForeignKey('ContactPerson.id'))
    relationType = Column(String(10), ForeignKey(
        'RelationshipDic.relationType'))
    POcode = Column(String(10))
    __table_args__ = (
        PrimaryKeyConstraint('customerId', 'contactId', 'relationType'),
    )


class CustomerDataManager:
    def __init__(self, session, idrecord, logging):
        '''
        :param session:
        :param idrecord:
        :param logging:
        '''
        self.session = session
        self.logging = logging
        pass

    def searchCustomer(self):
        '''
        :return:
        '''
        # result = session.query(User.username).filter(User.username == 'bob').all()  # [('bob',)]
        pass

    def insertCustomerAndContactPersonRelationship(self, data):
        '''
        向数据库中插入新的客户与联系人关系
        :param data:
        :return:
        '''
        newData = self.createCustomerAndContactPersonRelationship(data)
        try:
            self.session.add(newData)
        except Exception as e:
            self.logging.error(e)
            self.session.rollback()
        finally:
            self.logging.info('请重新检查数据插入')

    def insertContactPerson(self, data):
        '''

        :param data:
        :return:
        '''
        newData = self.createContactPerson(data)
        try:
            self.session.add(newData)
        except Exception as e:
            self.logging.error(e)
            self.session.rollback()
        finally:
            self.logging.info('请重新检查数据插入')

    def insertCustomer(self, data):
        '''
        向数据库中进行插入
        :param data:
        :return:
        '''
        newData = self.createCustomer(data)
        try:
            self.session.add(newData)
        except Exception as e:
            self.logging.error(e)
            self.session.rollback()
        finally:
            self.logging.info('请重新检查数据插入')

    def createCustomerAndContactPersonRelationship(self, data):
        '''
        创建新的客户与联系人关系
        :param data: 这个地方需要思考一下
        :return:
        '''
        newCustomerAndContactPersonRelationship = CustomerAndContactPersonRelationship(
            customerId=data['customerId'],
            contactId=data['contactId'],
            relationType=data['relationType'],
            POcode=data['Pocode']
        )
        return newCustomerAndContactPersonRelationship

    def createContactPerson(self, data):
        '''
        创建一个的ContactPerson ORM数据类
        :param data: 前端传过来的数据
        :return:
        '''
        newContactPerson = ContactPerson(
            name=data['name'],
            prefixName=data['prefixName'],
            first_name=data['first_name'],
            second_name=data['second_name'],
            language=data['language'],
            country=data['country'],
            area=data['area'],
            POcode=data['POcode']
        )
        return newContactPerson

    def createCustomer(self, data):
        '''
        将前端传过来的数据转化成ORM类
        :param data:
        :return:
        '''
        newCustomer = Customer(
            name=data['name'],
            street=data['street'],
            postcode=data['postcode'],
            country=data['country'],
            language=data['language'],
            accountantId=data['accountantId'],
            paycode=data['paycode'],
            distribution_channel=data['distribution_channel'],
            distribution_area=data['distribution_area'],
            sales_channel_number=data['sales_channel_number'],
            POcode=data['POcdoe']
        )
        return newCustomer
