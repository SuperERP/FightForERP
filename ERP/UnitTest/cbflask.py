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
    print(data)
    ret = {}
    if 'search' in data.keys():
        ret['data'] = newCustomer.searchCustomer()
    if 'create' in data.keys():
        '''
        根据销售订单创建发货单
        '''
        for item in data['data']:
            '''
            前端传来的销售订单数据
            '''
            print(item['salesOrderId'])
            saleOrderId = item['salesOrderId']
            plannedGIDate = item['plannedGIDate']
            salesOrder = newOrder.searchOrders(saleorderId=saleOrderId)
            warehouseId = salesOrder['warehouseId']
            print(plannedGIDate)
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
                newDelivery.insertDeliveryItem(newDeliveryItem)

    if 'seachcustomers' in data.keys():
        '''
        搜索所有用户
        '''
        ret['data'] = newCustomer.searchCustomer()

        return jsonify(ret)
    if 'seachsalesorders' in data.keys():
        '''
        搜索所有的销售订单
        '''
        ret['data'] = newOrder.searchOrders()
        print(ret)
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


# @app.route('/OutboundDeliveries/searchdelivery', methods=['post'])
# def createDeliverys():
#     '''
#     创建发货单
#     '''
#     pass

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
        newDelivery.deliveryOrder2to3(data['id'])
        return jsonify(ret)

    return jsonify(ret)


if __name__ == '__main__':
    app.run()
