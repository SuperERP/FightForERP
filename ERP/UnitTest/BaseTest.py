'''
用于优化基础设施
'''
from ERP.Modules.SuperErp import *
from ERP.Modules.WarehouseManager import WareHouseDataManager

warehouse = WareHouseDataManager(session, ErpLogger)
ordermanager = OrderManagerModule(session, ErpLogger)
'''
向数据库中插入所有的物料
'''
materialList = [
    {'id': 'sb101', 'name': 'mat1', 'price': 123},
    {'id': 'sb102', 'name': 'mat2', 'price': 123},
    {'id': 'sb103', 'name': 'mat3', 'price': 123},
    {'id': 'sb104', 'name': 'mat4', 'price': 123},
]

discountList = [
    {'id': 'zk101', 'name': 'zk1', 'discountCalcu': 'A'},
    {'id': 'zk102', 'name': 'zk2', 'discountCalcu': 'A'},
    {'id': 'zk103', 'name': 'zk3', 'discountCalcu': 'B'},
    {'id': 'zk104', 'name': 'zk4', 'discountCalcu': 'B'},

]
# warehouse.insetData()
Base.metadata.create_all()  # 将模型映射到数据库中
for i in materialList:
    warehouse.insertMaterialDic(i)
for i in discountList:
    ordermanager.insertDiscount(i)
session.commit()
