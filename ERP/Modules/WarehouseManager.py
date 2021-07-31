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

    def searchInventory(self, warehouseId='', materialDicId=''):
        '''
        根据条件查询库存
        '''
        res=[]

        for idata in self.session.query(Inventory).filter(or_(Inventory.materialDicId==materialDicId,materialDicId==''))\
                .filter(or_(Inventory.warehouseId==warehouseId,warehouseId=='')).all():
            res.append(self.to_dict(idata))

        return res
    
    def changeInventory(self,warehouseId, materialDicId, data :dict):
        '''
        修改库存信息
        '''
        try:
            self.session.query(Inventory).filter(Inventory.warehouseId==warehouseId).filter(Inventory.materialDicId==materialDicId).update(data)
            self.session.commit()
        except Exception as e:
            self.logging.info('请重新检查数据修改')
            self.logging.error(e)
            self.session.rollback()
    