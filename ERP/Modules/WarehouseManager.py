from .AbstractModule import *
from .OrmData.WareHouse import *


class WareHouseDataManager(AbstractModule):
    def __init__(self, session, logging):
        '''
        :param session:
        :param logging:
        '''

        super().__init__(session, logging)

    def insertInventory(self, data: dict):
        '''
        :param self:
        :param data:
        :return:
        '''
        newData = Inventory(**data)
        self.insertData(newData)

    def insertWarehouse(self, data: dict):
        '''
        插入库存数据
        :param data:
        :return:
        '''
        newData = Warehouse(**data)
        self.insertData(newData)


    def insertMaterialDic(self, data: dict):
        '''
        插入物料数据
        :param data:
        :return:
        '''
        newData = MaterialDic(**data)
        self.insertData(newData)

    def searchallWarehouse(self): 
        '''
        查找所有仓库信息
        '''
        res = []
        for item in self.session.query(Warehouse).all():
            res.append(self.to_dict(item))
        return res
    
    def searchallMaterialDic(self): 
        '''
        查询所有物料词条并添加相同单位EA
        '''
        res = []
        for item in self.session.query(MaterialDic).all():
            itemSp = self.to_dict(item)
            itemSp['salesUnit'] = 'EA'
            res.append(itemSp)
        return res

    def searchPrice(self, id):
        '''
        查询给定id的物料的价格
        '''
        res=[]

        for idata in self.session.query(MaterialDic).filter(MaterialDic.id == id).all():
            res.append(self.to_dict(idata))

        return res