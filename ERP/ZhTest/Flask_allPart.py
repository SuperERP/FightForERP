import sys
new_path = "/".join(sys.path[0].split('/')[:-1])
sys.path.append(new_path)
from flask_cors import CORS
from dateutil import parser
from flask import Flask, json, request
from flask import jsonify
from datetime import *
import os
import time
from Modules.SuperErp import *



newCustomer = CustomerManagerModule(session, ErpLogger)
newContactPerson = CustomerManagerModule(session, ErpLogger)
newBPrelationship = CustomerManagerModule(session, ErpLogger)
newWarehouseManager = WareHouseDataManager(session, ErpLogger)
newOrderManager = OrderManagerModule(session, ErpLogger)
newDelivery = DeliveryManagerModule(session, ErpLogger)

# 实例化产生一个Flask对象
app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/createCustomer', methods=['post'])  # 创建客户
def createCustomer():
    a = request.get_json()
    id = newCustomer.insertCustomer(a)
    return(id)


@app.route('/createContactPerson', methods=['post'])  # 创建联系人
def createContactPerson():
    a = request.get_json()
    try:
        id = newContactPerson.insertContactPerson(a)
    except Exception as e:
        return("fault")
    return(id)


@app.route('/createBPrelationship', methods=['post'])  # 创建客户联系人关系
def createBPrelationship():
    a = request.get_json()
    a['validTo'] = datetime.strptime(a['validTo'], '%Y-%m-%d')
    a['validFrom'] = datetime.strptime(a['validFrom'], '%Y-%m-%d')
    try:
        id = newBPrelationship.insertCustomerAndContactPersonRelationship(a)
    except Exception as e:
        return("fault")
    return(id)


@app.route('/showType', methods=['get'])  # 查询所有联系人类型
def showType():
    res = newBPrelationship.searchallRelationshipDic()
    return(jsonify(res))


@app.route('/showBPRelationship', methods=['get'])  # 查询所有BP关系
def showBPRelationship():
    res = newBPrelationship.searchallBPRelationship()
    return(jsonify(res))


@app.route('/searchBP1', methods=['post'])  # 按条件查询客户
def searchBP1():
    searchTerm = request.get_json()
    res = newBPrelationship.searchCustomer(POcode=searchTerm['POcode'], city=searchTerm['city'],
                                           country=searchTerm['country'], postcode=searchTerm['postcode'], name=searchTerm['name'])
    return(jsonify(res))


@app.route('/searchBP2', methods=['post'])  # 按条件查询联系人
def searchBP2():
    searchTerm = request.get_json()
    res = newBPrelationship.searchContactPerson(
        POcode=searchTerm['POcode'], last_name=searchTerm['last_name'], first_name=searchTerm['first_name'])
    return(jsonify(res))


@app.route('/searchCustomer', methods=['post'])  # 按id查询客户
def searchCustomer():
    searchTerm = list(request.form.to_dict().keys())[0]
    searchTerm = str(searchTerm).zfill(10)
    res = newBPrelationship.searchCustomer(id=searchTerm)[0]
    return(jsonify(res))


@app.route('/searchContactPerson', methods=['post'])  # 按id查询联系人
def searchContactPerson():
    searchTerm = list(request.form.to_dict().keys())[0]
    res = newBPrelationship.searchContactPerson(id=searchTerm)[0]
    return(jsonify(res))


@app.route('/searchBPRelationship', methods=['post'])  # 按id查询BP关系
def searchBPRelationship():
    searchTerm = list(request.form.to_dict().keys())[0]
    res = newBPrelationship.searchBPRelationship(id=searchTerm)[0]
    return(jsonify(res))


@app.route('/showWarehouse', methods=['get'])  # 查询所有仓库信息
def showWarehouse():
    res = newWarehouseManager.searchallWarehouse()
    return(jsonify(res))


@app.route('/showMaterialDic', methods=['get'])  # 查询所有物料词条
def showMaterialDic():
    res = newWarehouseManager.searchallMaterialDic()
    return(jsonify(res))


@app.route('/createInquiry', methods=['post'])  # 创建询价单及询价单物料项
def createInquiry():
    a = request.get_json()[0]
    b = request.get_json()[1]
    a['PODate'] = datetime.strptime(a['PODate'], '%Y-%m-%d')
    a['effectiveDate'] = datetime.strptime(a['effectiveDate'], '%Y-%m-%d')
    a['expirationDate'] = datetime.strptime(a['expirationDate'], '%Y-%m-%d')

    try:
        id = newOrderManager.insertInquiry(a)
        for item in b:
            item['inquiryId'] = id  # 把询价单编号加进询价单物料项的词条
            if 'price' in item:
                del item['price']
            newOrderManager.insertInquiryItem(item)
    except Exception as e:
        return("fault")
    return(id)


@app.route('/showDiscountDic', methods=['get'])  # 查询所有物料词条
def showDiscountDic():
    res = newOrderManager.searchallDiscountDic()
    return(jsonify(res))


@app.route('/createQuotation', methods=['post'])  # 创建报价单及报价单物料项
def createQuotation():
    a = request.get_json()[0]
    b = request.get_json()[1]
    a['PODate'] = datetime.strptime(a['PODate'], '%Y-%m-%d')
    a['effectiveDate'] = datetime.strptime(a['effectiveDate'], '%Y-%m-%d')
    a['expirationDate'] = datetime.strptime(a['expirationDate'], '%Y-%m-%d')
    a['requestedDeliveryDate'] = datetime.strptime(
        a['requestedDeliveryDate'], '%Y-%m-%d')
    if 'id' in a:
        del a['id']
    try:
        id = newOrderManager.insertQuotation(a)
        for item in b:
            item['quotationId'] = id  # 把报价单编号加进报价单物料项的词条
            if 'price' in item:
                del item['price']
            newOrderManager.insertQuotationItem(item)
    except Exception as e:
        print(e)
        return("fault")
    return(id)


@app.route('/createSalesOrder', methods=['post'])  # 创建销售订单及销售订单物料项
def createSalesOrder():
    a = request.get_json()[0]
    b = request.get_json()[1]
    a['PODate'] = datetime.strptime(a['PODate'], '%Y-%m-%d')
    a['effectiveDate'] = datetime.strptime(a['effectiveDate'], '%Y-%m-%d')
    a['expirationDate'] = datetime.strptime(a['expirationDate'], '%Y-%m-%d')
    a['requestedDeliveryDate'] = datetime.strptime(
        a['requestedDeliveryDate'], '%Y-%m-%d')
    if 'id' in a:
        del a['id']
    try:
        id = newOrderManager.createSalesOrder(a)
        for item in b:
            item['salesOrderId'] = id  # 把销售订单编号加进销售订单物料项的词条
            if 'price' in item:
                del item['price']
            newOrderManager.insertSalesOrderItem(item)
    except Exception as e:
        return("fault")
    return(id)


@app.route('/searchInquiry', methods=['post'])  # 按条件查找询价单
def searchInquiry():
    searchTerm = request.get_json()
    res = newOrderManager.searchInquiry(customerId=searchTerm['customerId'], warehouseId=searchTerm['warehouseId'], POcode=searchTerm['POcode'],
                                        PODate=searchTerm['PODate'], effectiveDate=searchTerm['effectiveDate'], expirationDate=searchTerm['expirationDate'])
    return(jsonify(res))


@app.route('/searchInquiryAndItem', methods=['post'])  # 按给定询价单号查找询价单及询价单物料项
def searchInquiryAndItem():
    searchTerm = request.get_json()
    res1 = newOrderManager.searchInquiry(id=searchTerm['id'])[0]
    res2 = newOrderManager.searchInquiryItem(inquiryId=searchTerm['id'])
    res = []
    res.append(res1)
    res.append(res2)
    return(jsonify(res))


# 按给定询价单号查找询价单及询价单物料项，页面预加载方法
@app.route('/searchInquiryAndItem2', methods=['post'])
def searchInquiryAndItem2():
    searchTerm = list(request.form.to_dict().keys())[0]
    res1 = newOrderManager.searchInquiry(id=searchTerm)[0]
    res2 = newOrderManager.searchInquiryItem(inquiryId=searchTerm)
    res = []
    res.append(res1)
    res.append(res2)
    return(jsonify(res))


@app.route('/searchQuotation', methods=['post'])  # 按条件查找报价单
def searchQuotation():
    searchTerm = request.get_json()
    res = newOrderManager.searchQuotation(customerId=searchTerm['customerId'], warehouseId=searchTerm['warehouseId'], POcode=searchTerm['POcode'],
                                          PODate=searchTerm['PODate'], effectiveDate=searchTerm['effectiveDate'], expirationDate=searchTerm['expirationDate'])
    return(jsonify(res))


@app.route('/searchQuotationAndItem', methods=['post'])  # 按给定报价单号查找报价单及报价单物料项
def searchQuotationAndItem():
    searchTerm = request.get_json()
    res1 = newOrderManager.searchQuotation(id=searchTerm['id'])[0]
    res2 = newOrderManager.searchQuotationItem(quotationId=searchTerm['id'])
    res = []
    res.append(res1)
    res.append(res2)
    return(jsonify(res))


# 按给定报价单号查找报价单及报价单物料项，页面预加载方法
@app.route('/searchQuotationAndItem2', methods=['post'])
def searchQuotationAndItem2():
    searchTerm = list(request.form.to_dict().keys())[0]
    res1 = newOrderManager.searchQuotation(id=searchTerm)[0]
    res2 = newOrderManager.searchQuotationItem(quotationId=searchTerm)
    res = []
    res.append(res1)
    res.append(res2)
    return(jsonify(res))


@app.route('/searchSalesOrder', methods=['post'])  # 按条件查找销售订单
def searchSalesOrder():
    searchTerm = request.get_json()
    res = newOrderManager.searchSalesOrder(customerId=searchTerm['customerId'], warehouseId=searchTerm['warehouseId'], POcode=searchTerm['POcode'],
                                           PODate=searchTerm['PODate'], effectiveDate=searchTerm['effectiveDate'], expirationDate=searchTerm['expirationDate'])
    return(jsonify(res))


# 按给定销售订单号查找销售订单及销售订单物料项，页面预加载方法
@app.route('/searchSalesOrderAndItem', methods=['post'])
def searchSalesOrderAndItem():
    searchTerm = list(request.form.to_dict().keys())[0]
    res1 = newOrderManager.searchSalesOrder(id=searchTerm)[0]
    res2 = newOrderManager.searchSalesOrderItem(salesOrderId=searchTerm)
    res = []
    res.append(res1)
    res.append(res2)
    return(jsonify(res))


@app.route('/changeCustomer', methods=['post'])  # 修改客户信息
def changeCustomer():
    a = request.get_json()
    id = a['id']
    if 'id' in a:
        del a['id']
    try:
        newCustomer.changeCustomer(id=id, data=a)
    except Exception as e:
        return("fault")
    return("success")


@app.route('/changeContactPerson', methods=['post'])  # 修改联系人信息
def changeContactPerson():
    a = request.get_json()
    id = a['id']
    if 'id' in a:
        del a['id']
    try:
        newContactPerson.changeContactPerson(id=id, data=a)
    except Exception as e:
        return("fault")
    return("success")


@app.route('/changeBPRelationship', methods=['post'])  # 修改BP关系
def changeBPRelationship():
    a = request.get_json()
    id = a['id']
    if 'id' in a:
        del a['id']
    a['validTo'] = datetime.strptime(a['validTo'], '%Y-%m-%d')
    a['validFrom'] = datetime.strptime(a['validFrom'], '%Y-%m-%d')
    try:
        newBPrelationship.changeBPRelationship(id=id, data=a)
    except Exception as e:
        return("fault")
    return("success")


@app.route('/changeInquiryAndItem', methods=['post'])  # 修改询价单及物料项
def changeInquiryAndItem():
    a = request.get_json()[0]
    b = request.get_json()[1]
    id = a['id']
    if 'id' in a:
        del a['id']
    a['PODate'] = datetime.strptime(a['PODate'], '%Y-%m-%d')
    a['effectiveDate'] = datetime.strptime(a['effectiveDate'], '%Y-%m-%d')
    a['expirationDate'] = datetime.strptime(a['expirationDate'], '%Y-%m-%d')

    try:
        newOrderManager.changeInquiry(id=id, data=a)
        for item in b:
            item['inquiryId'] = id
            if 'price' in item:
                del item['price']
            newOrderManager.insertInquiryItem(item)
    except Exception as e:
        return("fault")
    return("success")


@app.route('/changeQuotationAndItem', methods=['post'])  # 修改报价单及物料项
def changeQuotationAndItem():
    a = request.get_json()[0]
    b = request.get_json()[1]
    id = a['id']
    if 'id' in a:
        del a['id']
    a['PODate'] = datetime.strptime(a['PODate'], '%Y-%m-%d')
    a['effectiveDate'] = datetime.strptime(a['effectiveDate'], '%Y-%m-%d')
    a['expirationDate'] = datetime.strptime(a['expirationDate'], '%Y-%m-%d')
    a['requestedDeliveryDate'] = datetime.strptime(
        a['requestedDeliveryDate'], '%Y-%m-%d')

    try:
        newOrderManager.changeQuotation(id=id, data=a)
        for item in b:
            item['quotationId'] = id
            if 'price' in item:
                del item['price']
            newOrderManager.insertQuotationItem(item)
    except Exception as e:
        return("fault")
    return("success")


@app.route('/changeSalesOrderAndItem', methods=['post'])  # 修改销售订单及物料项
def changeSalesOrderAndItem():
    a = request.get_json()[0]
    b = request.get_json()[1]
    id = a['id']
    if 'id' in a:
        del a['id']
    a['PODate'] = datetime.strptime(a['PODate'], '%Y-%m-%d')
    a['effectiveDate'] = datetime.strptime(a['effectiveDate'], '%Y-%m-%d')
    a['expirationDate'] = datetime.strptime(a['expirationDate'], '%Y-%m-%d')
    a['requestedDeliveryDate'] = datetime.strptime(
        a['requestedDeliveryDate'], '%Y-%m-%d')

    try:
        newOrderManager.changeSalesOrder(id=id, data=a)
        for item in b:
            item['salesOrderId'] = id
            if 'price' in item:
                del item['price']
            newOrderManager.insertSalesOrderItem(item)
    except Exception as e:
        return("fault")
    return("success")


@app.route('/searchInventory', methods=['post'])  # 按条件查找库存
def searchInventory():
    searchTerm = request.get_json()
    res = newWarehouseManager.searchInventory(
        warehouseId=searchTerm['warehouseId'], materialDicId=searchTerm['materialDicId'])
    return(jsonify(res))


@app.route('/changeInventory', methods=['post'])  # 更改库存
def changeInventory():
    a = request.get_json()
    try:
        for item in a:
            iwarehouseId = item['warehouseId']
            imaterialDicId = item['materialDicId']
            if 'warehouseId' in item:
                del item['warehouseId']
            if 'materialDicId' in item:
                del item['materialDicId']
            newWarehouseManager.changeInventory(
                warehouseId=iwarehouseId, materialDicId=imaterialDicId, data=item)
    except Exception as e:
        return("fault")
    return("success")


@app.route('/CreateOutboundDeliveries', methods=['post'])
def CreateOutboundDeliveries():
    data = request.get_json(silent=True)
    ret = {}
    if 'warehouse' in data.keys():
        res = newWarehouseManager.searchallWarehouse()
        ret['data'] = []
        for item in res:
            ret['data'].append(item['id'])
        return jsonify(ret)

    if 'go' in data.keys():
        if len(data['shippingpoints']) == 0:
            ret['data'] = newOrderManager.searchOrders(
                customerId=data['customerId'], saleorderId=data['saleorderId'], effectiveDate=data['date'])
        else:
            ret['data'] = newOrderManager.searchOrders(
                customerId=data['customerId'], saleorderId=data['saleorderId'], effectiveDate=data['date'], warehouseId=data['shippingpoints'], flag=True)
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
            salesOrder = newOrderManager.searchOrders(saleorderId=saleOrderId)
            warehouseId = salesOrder['warehouseId']
            deliveryOrder = {
                'plannedDeliveryTime': parser.parse(plannedGIDate),
                'deliveryPhase': 0,
                'salesOrderId': saleOrderId,
                'warehouseId': warehouseId,
                'actualDeliveryTime': None
            }
            deliveryOrderId = newDelivery.insertDeliveryOrder(deliveryOrder)

            salesOrderItems = newOrderManager.searchAllSalesOrderItems(
                saleOrderId=saleOrderId)
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
                flag = newWarehouseManager.createDelivery(
                    materialId=item.material, warehouseId=warehouseId, count=item.amount)
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

        ret['data'] = newOrderManager.searchOrders(
            customerId=data['customerId'], warehouseId=data['warehouseId'])
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


@app.route('/PickingOutboundDelivery', methods=['post'])
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
            saleOrderItem = newOrderManager.searchOrders(
                saleorderId=saleOrderId)

            # 字典拼接
            tDict = {k: v for k, v in deliveryItem.items()}
            tDict['customerName'] = saleOrderItem['customerName']
            tDict['warehouseName'] = saleOrderItem['warehouseName']
            ret['data'].append(tDict)
        print(ret)
        return jsonify(ret)

    if 'picking' in data.keys():
        for item in data['pickingitems']:
            newDelivery.pickingDeliveryItems(
                materialId=item['MaterialId'], deliveryOrderId=item['DeliveryOrder'])
        ret['data'] = newDelivery.searchDeliveryItems(data['id'])

        return jsonify(ret)

    if '2to3' in data.keys():
        datestr = data['date']
        '''
        发货并完成库存部分的管理
        data['id']指的是发货单的id
        '''

        newDelivery.deliveryOrder2to3(data['id'], datestr)

        newWarehouseManager.deliveryOrder2to3()

        return jsonify(ret)

    return jsonify(ret)


if __name__ == '__main__':
    app.run()