import sys

new_path = "/".join(sys.path[0].split('/')[:-1])
sys.path.append(new_path)

from Modules.SuperErp import *
from Modules.WarehouseManager import WareHouseDataManager

newCustomer = CustomerManagerModule(session, ErpLogger)
newDelivery = DeliveryManagerModule(session, ErpLogger)
newOrder = OrderManagerModule(session, ErpLogger)
newware = WareHouseDataManager(session, ErpLogger)

Base.metadata.create_all()  # 将模型映射到数据库中

materialList = [
    {'id': 'Material101', 'name': 'Mat1', 'price': 60},
    {'id': 'Material102', 'name': 'Mat2', 'price': 70},
    {'id': 'Material103', 'name': 'Mat3', 'price': 80},
    {'id': 'Material104', 'name': 'Mat4', 'price': 90},
]

discountList = [
    {'id': 'Discount101', 'name': 'K004', 'discountCalcu': 'Quantification'},
    {'id': 'Discount102', 'name': 'RA00', 'discountCalcu': 'Percentage'},
]

warehouse = [
    {'id': 'SH00', 'name': 'ShangHai'},
    {'id': 'MI00', 'name': 'Miami'},
    {'id': 'SY00', 'name': 'Sydney'},
    {'id': 'BE00', 'name': 'Berlin'}
]

inventorys=[
    {
        'warehouseId':'SH00',
        'materialDicId':'Material101',
        'volume':500000,
        'requestVolume':0,
        'onOrderStock':0
    },
    {
        'warehouseId':'SH00',
        'materialDicId':'Material102',
        'volume':500000,
        'requestVolume':0,
        'onOrderStock':0
    },
    {
        'warehouseId':'SH00',
        'materialDicId':'Material103',
        'volume':500000,
        'requestVolume':0,
        'onOrderStock':0
    },
    {
        'warehouseId':'MI00',
        'materialDicId':'Material101',
        'volume':500000,
        'requestVolume':0,
        'onOrderStock':0
    },
    {
        'warehouseId':'BE00',
        'materialDicId':'Material102',
        'volume':500000,
        'requestVolume':0,
        'onOrderStock':0
    }
]

customerList = [
    {
        'id':'0001100000',
        'name':'CrazyDaff',
        'street':'SiPing',
        'postcode':'130031',
        'country':'CH',
        'language':'CN',
        'city':'ShangHai',
        'region':'ShangHai',
        'distribution_channel':'SD00',
        'sales_channel_number':'',
        'POcode':'030'
    },
    {
        'id':'0001100001',
        'name':'CrazyDaff',
        'street':'SiPing',
        'postcode':'130031',
        'country':'CH',
        'language':'CN',
        'city':'ShangHai',
        'region':'ShangHai',
        'distribution_channel':'SD00',
        'sales_channel_number':'',
        'POcode':'031'
    },
    {
        'id':'0001100002',
        'name':'CrazyDaff',
        'street':'SiPing',
        'postcode':'130031',
        'country':'CH',
        'language':'CN',
        'city':'ShangHai',
        'region':'ShangHai',
        'distribution_channel':'SD00',
        'sales_channel_number':'',
        'POcode':'032'
    },
    {
        'id':'0001100003',
        'name':'CrazyDaff',
        'street':'SiPing',
        'postcode':'130031',
        'country':'CH',
        'language':'CN',
        'city':'ShangHai',
        'region':'ShangHai',
        'distribution_channel':'SD00',
        'sales_channel_number':'',
        'POcode':'033'
    },
    {
        'id':'0001100004',
        'name':'CrazyDaff',
        'street':'SiPing',
        'postcode':'130031',
        'country':'CH',
        'language':'CN',
        'city':'ShangHai',
        'region':'ShangHai',
        'distribution_channel':'SD00',
        'sales_channel_number':'',
        'POcode':'034'
    },
]

for i in materialList:
    newware.insertMaterialDic(i)
for i in discountList:
    newOrder.insertDiscount(i)
for idata in warehouse:
    newware.insertWarehouse(idata)
for item in inventorys:
    newware.insertInventory(item)
for i in customerList:
    newCustomer.insertCustomer2(i)