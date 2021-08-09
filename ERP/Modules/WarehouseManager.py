from .AbstractModule import *
from .OrmData.WareHouse import *
from .OrmData.QutationAndSalesOrderData import *
from .OrmData.DeliveryData import *


class WareHouseDataManager(AbstractModule):
    def __init__(self, session, logging):
        '''
        :param session:
        :param logging:
        '''

        super().__init__(session, logging)

    def createDelivery(self, materialId=None, count=None, warehouseId=None):
        '''
        根据发货单修改库存的容量
        如果数量不够时不能发货的
        '''

        try:
            print(materialId, warehouseId)
            amount = self.session.query(Inventory).filter(
                and_(Inventory.warehouseId == warehouseId, Inventory.materialDicId == materialId)).all()[0].volume
            print('amount', amount)
            print(count)
            if (amount < count):
                return False
            else:
                self.session.query(Inventory).filter(and_(Inventory.warehouseId == warehouseId, Inventory.materialDicId == materialId)).update(
                    {
                        Inventory.volume: Inventory.volume - count,
                        Inventory.onOrderStock: Inventory.onOrderStock + count
                    }
                )
                self.session.commit()
                

        except Exception:
            self.logging.error(e)
            self.logging.info('发生问题')

            return False

    def delivery1to2(self, deliveryOrderId=None, materialId=None):
        try:
            warehouseId = self.session.query(DeliveryOrder).filter(
                DeliveryOrder.id == deliveryOrderId).all()[0].warehouseId

            deliveryItemAmount = self.session.query(DeliveryItem).filter(and_(
                DeliveryItem.deliveryOrderId == deliveryOrderId, DeliveryItem.materialId == materialId)).all()[0].amount
            self.session.query(Inventory).filter(and_(Inventory.warehouseId == warehouseId, Inventory.materialDicId == materialId)).update(
                {
                    Inventory.requestVolume: Inventory.requestVolume-deliveryItemAmount,
                    Inventory.onOrderStock: Inventory.onOrderStock+deliveryItemAmount
                }
            )
            self.session.commit()
        except Exception as e:
            self.session.error(e)
        self.logging.info('1t02 finished')

    def deliveryOrder2to3(self, deliverOrderId=None):
        '''
        完成库存管理部分发货阶段的转换
        '''
        try:
            '''
            搜寻所有的发货单物料项，并且物料项已经处于拣配状态
            '''
            data = self.session.query(DeliveryItem).filter(DeliveryItem.deliveryOrderId == deliverOrderId).filter(
                DeliveryItem.pickingStatus == 1).all()
            print(data)
            warehouseId=self.session.query(DeliveryOrder).filter(DeliveryOrder.id==deliverOrderId).all()[0].warehouseId
            for item in data:
                count = item.amount
                self.session.query(Inventory).filter(and_(Inventory.materialDicId == item.materialId,Inventory.warehouseId==warehouseId)).update(
                    {
                        Inventory.onOrderStock: Inventory.onOrderStock - count,
                    }
                )
            self.session.commit()
            self.logging.info('库存管理完成')
        except Exception as e:
            self.logging.info('发生错误')
            self.logging.error(e)

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
        res = []

        for idata in self.session.query(MaterialDic).filter(MaterialDic.id == id).all():
            res.append(self.to_dict(idata))

        return res

    def searchInventory(self, warehouseId='', materialDicId=''):
        '''
        根据条件查询库存
        '''
        res = []

        for idata in self.session.query(Inventory).filter(or_(Inventory.materialDicId == materialDicId, materialDicId == ''))\
                .filter(or_(Inventory.warehouseId == warehouseId, warehouseId == '')).all():
            res.append(self.to_dict(idata))

        return res

    def changeInventory(self, warehouseId, materialDicId, data: dict):
        '''
        修改库存信息
        '''
        try:
            self.session.query(Inventory).filter(Inventory.warehouseId == warehouseId).filter(
                Inventory.materialDicId == materialDicId).update(data)
            self.session.commit()
        except Exception as e:
            self.logging.info('请重新检查数据修改')
            self.logging.error(e)
            self.session.rollback()

    def toSale(self, warehouseId, materialDicId, amount):
        '''
        检查并根据销售订单修改库存
        '''
        volume = self.session.query(Inventory).filter(Inventory.warehouseId == warehouseId).filter(
            Inventory.materialDicId == materialDicId).all()[0].volume
        requestVolume = self.session.query(Inventory).filter(Inventory.warehouseId == warehouseId).filter(
            Inventory.materialDicId == materialDicId).all()[0].requestVolume
        if volume >= amount:
            self.session.query(Inventory).filter(Inventory.warehouseId == warehouseId).filter(
                Inventory.materialDicId == materialDicId).update({'volume': volume-amount, 'requestVolume': amount+requestVolume})
        else:
            return "fault"
        return "success"
