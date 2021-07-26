# from ..Modules.SuperErp import *
import sys

new_path = "/".join(sys.path[0].split('/')[:-2])
sys.path.append(new_path)

from ERP.Modules.SuperErp import *
import time
import os
from datetime import date

from ERP.Modules.WarehouseManager import WareHouseDataManager

newCustomer = CustomerManagerModule(session, ErpLogger)

newDelivery = DeliveryManagerModule(session, ErpLogger)
newOrder = OrderManagerModule(session, ErpLogger)
newware = WareHouseDataManager(session, ErpLogger)

# os.remove('/home/supercb/PycharmProjects/FightForERP/ERP/UnitTest/tutorial.db')

nc = {}
nc['name'] = 'zht'
nc['street'] = "sp"
nc['postcode'] = "111"
nc['country'] = "CN"
nc['language'] = "CH"
nc['accountantId'] = "185324"
nc['paycode'] = "1853245"
nc['distribution_channel'] = "00"
nc['distribution_area'] = "CN00"
nc['sales_channel_number'] = "0"
nc['POcode'] = "123"
newCustomer.insertCustomer(nc)

pocode = '036'
date1 = date(2010, 12, 31)

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
    newware.insertMaterialDic(i)
for i in discountList:
    newOrder.insertDiscount(i)

warehouse = [
    {'id': 'lz101', 'name': 'mat1'},
    {'id': 'lz102', 'name': 'mat2'},
    {'id': 'lz103', 'name': 'mat2'},
    {'id': 'lz104', 'name': 'mat2'}
]
for idata in warehouse:
    newware.insertWarehouse(idata)
salesOrders = [
    {
        'customerId': '0001000000',
        'warehouseId': 'lz101',
        'POcode': pocode,
        'PODate': date1,
        'effectiveDate': date1,
        'expirationDate': date1,
        'requestedDeliveryDate': date1,
        'discountId': 'zk101',
        'totalDiscountNum': 10
    }
]
for idata in salesOrders:
    newOrder.createSalesOrder(idata)
deliverys = [
    {
        'plannedDeliveryTime': date1,
        'actualDeliveryTime': None,
        'salesOrderId': 'SO20211052460726',
        'warehouseId': 'lz101',
        'deliveryPhase': '1'
    },
    {
        'plannedDeliveryTime': date1,
        'actualDeliveryTime': None,
        'salesOrderId': 'SO20211052460726',
        'warehouseId': 'lz101',
        'deliveryPhase': '1'
    },
    {
        'plannedDeliveryTime': date1,
        'actualDeliveryTime': None,
        'salesOrderId': 'SO20211052460726',
        'warehouseId': 'lz101',
        'deliveryPhase': '1'
    }
]
for idata in deliverys:
    newDelivery.insertDeliveryOrder(idata)
print(type(newDelivery.searchallDelivery()[0]))