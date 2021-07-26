from .AbstractModule import*
from .OrmData.CustomerData import *


class CustomerManagerModule(AbstractModule):
    def __init__(self, session, logging, customerRecord=1000000):
        '''
        :param session:
        :param idrecord:
        :param logging:
        '''
        super().__init__(session, logging)
        self.session = session
        self.logging = logging
        self.customerRecord = customerRecord

    def searchCustomer(self,searchTerm=None,city=None):
        '''
        :return:
        '''
        # result = session.query(User.username).filter(User.username == 'bob').all()  # [('bob',)]
        if(searchTerm!=None and city!=None):
            pass

        res=[]

        for idata in self.session.query(Customer).all():
            res.append(self.to_dict(idata))

        return res

    def insertCustomerAndContactPersonRelationship(self, data: dict):
        '''
        向数据库中插入新的客户与联系人关系
        :param data:
        :return:
        '''

        new_data = CustomerAndContactPersonRelationship(**data)
        self.insertData(new_data)

    def insertContactPerson(self, data: dict):
        '''

        :param data:
        :return:
        '''
        Base.metadata.create_all()
        data['id'] = 'CP' + self.getTimeId()
        new_data = ContactPerson(**data)
        self.insertData(new_data)

    def insertCustomer(self, data: dict):
        '''
        向数据库中进行插入
        :param data:
        :return:
        '''
        Base.metadata.create_all()
        data['id'] = str(self.customerRecord).zfill(10)
        new_data = Customer(**data)
        if self.insertData(new_data):
            self.customerRecord += 1
        return data['id']
