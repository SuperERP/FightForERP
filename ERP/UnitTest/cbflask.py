import sys

import dateutil

new_path = "/".join(sys.path[0].split('/')[:-1])
sys.path.append(new_path)
from flask_cors import CORS
from flask import Flask, request
from ERP.Modules.WarehouseManager import WareHouseDataManager
from flask import jsonify
from datetime import date, datetime
from dateutil import parser
import os
import time
from ERP.Modules.SuperErp import *

newCustomer = CustomerManagerModule(session, ErpLogger)

newDelivery = DeliveryManagerModule(session, ErpLogger)
newOrder = OrderManagerModule(session, ErpLogger)
newware = WareHouseDataManager(session, ErpLogger)

# 实例化产生一个Flask对象

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/CreateOutboundDeliveries', methods=['post'])
def CreateOutboundDeliveries():
    data = request.get_json(silent=True)
    ret = {}
    if 'go' in data.keys():
        if 'saleorderId' in data.keys() and data['saleorderId'] != '':
            ret['data'] = [newOrder.searchOrders(saleorderId=data['saleorderId'])]
        else:
            ret['data'] = newOrder.searchOrders(customerId=data['customerId'])
        return jsonify(ret)
    if 'create' in data.keys():
        '''
        根据销售订单创建发货单
        '''
        for item in data['data']:
            '''
            前端传来的销售订单数据
            '''
            saleOrderId = item['salesOrderId']
            plannedGIDate = item['plannedGIDate']
            salesOrder = newOrder.searchOrders(saleorderId=saleOrderId)
            warehouseId = salesOrder['warehouseId']
            deliveryOrder = {
                'plannedDeliveryTime': parser.parse(plannedGIDate),
                'deliveryPhase': 0,
                'salesOrderId': saleOrderId,
                'warehouseId': warehouseId,
                'actualDeliveryTime': None
            }
            deliveryOrderId = newDelivery.insertDeliveryOrder(deliveryOrder)

            salesOrderItems = newOrder.searchAllSalesOrderItems(saleOrderId=saleOrderId)
            for item in salesOrderItems:
                '''
                创建发货单物料项 
                '''
                newDeliveryItem = {
                    'deliveryOrderId': deliveryOrderId,
                    'materialId': item.material,
                    'description': item.itemDescription,
                    'amount': item.amount,
                    'unit': item.salesUnit,
                    'pickingAmount': 0,
                    'pickingStatus': 0,
                    'materialState': 0,
                }
                '''
                处理库存的问题
                '''
                flag = newware.createDelivery(materialId=item.material, warehouseId=warehouseId, count=item.amount)
                if flag is False:
                    '''
                    失败则返回有问题
                    '''
                    ret['flag'] = False
                    return jsonify(ret)
                newDelivery.insertDeliveryItem(newDeliveryItem)

        ret['flag'] = True
        return jsonify(ret)
    if 'seachcustomers' in data.keys():
        '''
        搜索所有用户
        '''

        ret['data'] = newCustomer.searchCustomer(POcode=data['pocode'])

        return jsonify(ret)
    if 'seachsalesorders' in data.keys():
        '''
        搜索所有的销售订单
        '''

        ret['data'] = newOrder.searchOrders(customerId=data['customerId'], warehouseId=data['warehouseId'])
        return jsonify(ret)
    return jsonify(ret)


@app.route('/OutboundDeliveries/searchdelivery', methods=['post'])
def finddelivery():
    data = request.get_json(silent=True)
    print(data)
    ret = {}
    ret['data'] = newDelivery.searchallDelivery()
    print(ret)
    return jsonify(ret)


@app.route('/PickingOutboundDelivery1', methods=['post'])
def PickingOutboundDelivery():
    '''
    寻找销售订单物料项
    '''
    data = request.get_json(silent=True)
    ret = {}
    print(data)
    if 'jump' in data.keys():
        ret['data'] = newDelivery.searchDeliveryItems(data['id'])
        return jsonify(ret)

    if 'search' in data.keys():
        '''
        寻找发货单
        '''

        ret['data'] = []
        deliveryOrders = newDelivery.searchallDelivery()
        for deliveryItem in deliveryOrders:
            print(deliveryItem)

            saleOrderId = deliveryItem['salesOrderId']
            saleOrderItem = newOrder.searchOrders(saleorderId=saleOrderId)

            # 字典拼接
            tDict = {k: v for k, v in deliveryItem.items()}
            tDict['customerName'] = saleOrderItem['customerName']
            tDict['warehouseName'] = saleOrderItem['warehouseName']
            ret['data'].append(tDict)
        print(ret)
        return jsonify(ret)

    if 'picking' in data.keys():
        for item in data['pickingitems']:
            newDelivery.pickingDeliveryItems(materialId=item['Item'], deliveryOrderId=item['DeliveryOrder'])
        ret['data'] = newDelivery.searchDeliveryItems(data['id'])

        return jsonify(ret)

    if '2to3' in data.keys():
        datestr = data['date']
        '''
        发货并完成库存部分的管理
        data['id']指的是发货单的id
        '''

        newDelivery.deliveryOrder2to3(data['id'], datestr)

        newware.deliveryOrder2to3()

        return jsonify(ret)

    return jsonify(ret)


if __name__ == '__main__':
    app.run()
