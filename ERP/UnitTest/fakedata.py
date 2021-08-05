# from ..Modules.SuperErp import *


import sys

from sqlalchemy.sql.functions import random

new_path = "/".join(sys.path[0].split('/')[:-1])
sys.path.append(new_path)

from Modules.SuperErp import *
import time
import os
from datetime import date
from Modules.WarehouseManager import WareHouseDataManager

newCustomer = CustomerManagerModule(session, ErpLogger)

newDelivery = DeliveryManagerModule(session, ErpLogger)
newOrder = OrderManagerModule(session, ErpLogger)
newware = WareHouseDataManager(session, ErpLogger)

# os.remove('/home/supercb/PycharmProjects/NewErp/ERP/UnitTest/tutorial.db')

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
nc['city'] = 'dsafdsfs'
nc['POcode'] = "123"
nc['region'] = 'sdfsd'

newCustomer.insertCustomer(nc)

pocode = '036'
ttime = time.localtime()
date1 = date(2010, 12, 7)

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
        'totalDiscountNum': 10,
        'cnty': '12312',
        'totalCntyPercent': '2312'

    }, {
        'customerId': '0001000000',
        'warehouseId': 'lz101',
        'POcode': pocode,
        'PODate': date1,
        'effectiveDate': date1,
        'expirationDate': date1,
        'requestedDeliveryDate': date1,
        'discountId': 'zk101',
        'totalDiscountNum': 10,
        'cnty': '12312',
        'totalCntyPercent': '2312'

    }, {
        'customerId': '0001000000',
        'warehouseId': 'lz101',
        'POcode': pocode,
        'PODate': date1,
        'effectiveDate': date1,
        'expirationDate': date1,
        'requestedDeliveryDate': date1,
        'discountId': 'zk101',
        'totalDiscountNum': 10,
        'cnty': '12312',
        'totalCntyPercent': '2312'

    }, {
        'customerId': '0001000000',
        'warehouseId': 'lz101',
        'POcode': pocode,
        'PODate': date1,
        'effectiveDate': date1,
        'expirationDate': date1,
        'requestedDeliveryDate': date1,
        'discountId': 'zk101',
        'totalDiscountNum': 10,
        'cnty': '12312',
        'totalCntyPercent': '2312'
    }
]
for idata in salesOrders:
    newOrder.createSalesOrder(idata)

deliverys = []
import random

for item in session.query(SalesOrder).all():
    id = item.id
    tdata = {}
    tdata['salesOrderId'] = id
    tdata['plannedDeliveryTime'] = date1
    tdata['actualDeliveryTime'] = None
    tdata['warehouseId'] = 'lz101'
    tdata['deliveryPhase'] = 1
    deliverys.append(tdata)

for idata in deliverys:
    newDelivery.insertDeliveryOrder(idata)
print(type(newDelivery.searchallDelivery()[0]))
delid = session.query(DeliveryOrder).all()[0].id
newDeliveryItems = [
    {
        'deliveryOrderId': delid,
        'materialId': 'sb101',
        'description': 'sdfsdfasd',
        'amount': 10,
        'unit': '3213123'
        , 'pickingStatus': 0,
        'pickingAmount': 210,
        'materialState': 'sadfsd'
    },
    {
        'deliveryOrderId': delid,
        'materialId': 'sb102',
        'description': 'sdfsdfasd',
        'amount': 10,
        'unit': '3213123'
        , 'pickingStatus': 1,
        'pickingAmount': 111,
        'materialState': 'sadfsd'
    }, {
        'deliveryOrderId': delid,
        'materialId': 'sb103',
        'description': 'sdfsdfasd',
        'amount': 10,
        'unit': '3213123'
        , 'pickingStatus': 1,
        'pickingAmount': 101,
        'materialState': 'sadfsd'
    },
    {
        'deliveryOrderId': delid,
        'materialId': 'sb104',
        'description': 'sdfsdfasd',
        'amount': 10,
        'unit': '3213123',
        'pickingStatus': 0,
        'pickingAmount': 110,
        'materialState': 'sadfsd'
    }
]

for idata in session.query(SalesOrder).all():
    for idata1 in session.query(MaterialDic).all():
        item = {
            'salesOrderId': idata.id,
            'material': idata1.id,
            'itemDescription': '22232323',
            'orderQuantity': 'dfsdf',
            'salesUnit': '00000',
            'cnty': '12312',
            'amount': 12312
        }
        newOrder.insertSalesOrderItem(item)

for idata in newDeliveryItems:
    newDelivery.insertDeliveryItem(idata)
