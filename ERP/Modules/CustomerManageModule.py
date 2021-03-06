from .AbstractModule import *
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

    def searchallRelationshipDic(self):
        '''
        查找所有关系字典
        '''
        res = []
        for item in self.session.query(RelationshipDic).all():
            res.append(self.to_dict(item))
        return res

    def searchCustomer(self,id='',POcode='',city='',country='',postcode='',name=''):
        '''
        按条件查找客户，空条件表示所有
        :return:
        '''

        res = []

        for idata in self.session.query(Customer).filter(or_(Customer.POcode==POcode,POcode==''))\
            .filter(or_(Customer.city==city,city==''))\
                .filter(or_(Customer.country==country,country==''))\
                    .filter(or_(Customer.postcode==postcode,postcode==''))\
                        .filter(or_(Customer.id==id,id==''))\
                            .filter(or_(Customer.name==name,name=='')).all():
            res.append(self.to_dict(idata))

        return res

    def searchContactPerson(self,id='',POcode='',last_name='',first_name=''):
        '''
        按条件查找联系人，空条件表示所有
        :return:
        '''

        res = []

        for idata in self.session.query(ContactPerson).filter(or_(ContactPerson.POcode==POcode,POcode==''))\
            .filter(or_(ContactPerson.last_name==last_name,last_name==''))\
                .filter(or_(ContactPerson.id==id,id==''))\
                    .filter(or_(ContactPerson.first_name==first_name,first_name=='')).all():
            res.append(self.to_dict(idata))

        return res

    def searchBPRelationship(self,id=''):
        '''
        按id查找BP关系
        :return:
        '''

        res=[]

        for idata in self.session.query(CustomerAndContactPersonRelationship).filter(CustomerAndContactPersonRelationship.id==id).all():
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
        return (data['id'])

    def insertContactPerson(self, data: dict):
        '''
        插入联系人信息
        :param data:
        :return:
        '''
        Base.metadata.create_all()
        data['id'] = 'CP' + self.getTimeId()
        new_data = ContactPerson(**data)
        self.insertData(new_data)
        return (data['id'])

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

    def searchallBPRelationship(self): 
        '''
        查找所有BP关系
        '''
        res = []
        for item in self.session.query(CustomerAndContactPersonRelationship).all():
            res.append(self.to_dict(item))
        return res

    def changeCustomer(self,id, data :dict):
        '''
        修改用户信息
        '''
        try:
            self.session.query(Customer).filter(Customer.id==id).update(data)
            self.session.commit()
        except Exception as e:
            self.logging.info('请重新检查数据修改')
            self.logging.error(e)
            self.session.rollback()

    def changeContactPerson(self,id, data :dict):
        '''
        修改联系人信息
        '''
        try:
            self.session.query(ContactPerson).filter(ContactPerson.id==id).update(data)
            self.session.commit()
        except Exception as e:
            self.logging.info('请重新检查数据修改')
            self.logging.error(e)
            self.session.rollback()
    
    def changeBPRelationship(self,id, data :dict):
        '''
        修改BP关系
        '''
        try:
            self.session.query(CustomerAndContactPersonRelationship).filter(CustomerAndContactPersonRelationship.id==id).update(data)
            self.session.commit()
        except Exception as e:
            self.logging.info('请重新检查数据修改')
            self.logging.error(e)
            self.session.rollback()
 
    def insertCustomer2(self, data: dict):
        '''
        向数据库中进行插入*****假数据专用*****
        :param data:
        :return:
        '''
        Base.metadata.create_all()
        new_data = Customer(**data)
        if self.insertData(new_data):
            self.customerRecord += 1
        return data['id']