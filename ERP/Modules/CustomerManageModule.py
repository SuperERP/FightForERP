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
    
    def searchallRelationshipDic(self): # 查找所有关系字典
        res = []
        for item in self.session.query(RelationshipDic).all():
            res.append(self.to_dict(item))
        return res

    def searchCustomer(self,POcode=None,city=None,country=None,postcode=None,name=None):
        '''
        :return:
        '''

        res=[]

        for idata in self.session.query(Customer).filter(or_(Customer.POcode==POcode,POcode==''))\
            .filter(or_(Customer.city==city,city==''))\
                .filter(or_(Customer.country==country,country==''))\
                    .filter(or_(Customer.postcode==postcode,postcode==''))\
                        .filter(or_(Customer.name==name,name=='')).all():
            res.append(self.to_dict(idata))

        return res

    def searchContactPerson(self,POcode=None,last_name=None,first_name=None):
        '''
        :return:
        '''

        res=[]

        for idata in self.session.query(ContactPerson).filter(or_(ContactPerson.POcode==POcode,POcode==''))\
            .filter(or_(ContactPerson.last_name==last_name,last_name==''))\
                .filter(or_(ContactPerson.first_name==first_name,first_name=='')).all():
            res.append(self.to_dict(idata))

        return res
        
    def insertCustomerAndContactPersonRelationship(self, data: dict):
        '''
        向数据库中插入新的客户与联系人关系
        :param data:
        :return:
        '''
        Base.metadata.create_all()
        data['id'] = 'BP' + self.getTimeId()
        new_data = CustomerAndContactPersonRelationship(**data)
        self.insertData(new_data)
        return(data['id'])

    def insertContactPerson(self, data: dict):
        '''

        :param data:
        :return:
        '''
        Base.metadata.create_all()
        data['id'] = 'CP' + self.getTimeId()
        new_data = ContactPerson(**data)
        self.insertData(new_data)
        return(data['id'])

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
