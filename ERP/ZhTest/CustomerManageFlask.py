import sys

new_path = "/".join(sys.path[0].split('/')[:-1])
sys.path.append(new_path)

from ERP.Modules.SuperErp import *
import time
import os
from datetime import *
from flask import jsonify
from flask import Flask, request
from flask_cors import CORS

newCustomer = CustomerManagerModule(session, ErpLogger)
newContactPerson = CustomerManagerModule(session, ErpLogger)
newBPrelationship = CustomerManagerModule(session, ErpLogger)
newWarehouseManager = WareHouseDataManager(session,ErpLogger)
newOrderManager = OrderManagerModule(session,ErpLogger)

# 实例化产生一个Flask对象
app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/createCustomer', methods=['post']) # 创建客户
def createCustomer():
    a = request.get_json()
    id = newCustomer.insertCustomer(a)
    return(id)

@app.route('/createContactPerson', methods=['post']) # 创建联系人
def createContactPerson():
    a = request.get_json()
    try:
        id = newContactPerson.insertContactPerson(a)
    except Exception as e:
        return("false")
    return(id)

@app.route('/createBPrelationship', methods=['post']) # 创建客户联系人关系
def createBPrelationship():
    a = request.get_json()
    a['validTo'] = datetime.strptime(a['validTo'],'%Y-%m-%d')
    a['validFrom'] = datetime.strptime(a['validFrom'],'%Y-%m-%d')
    try:
        id = newBPrelationship.insertCustomerAndContactPersonRelationship(a)
    except Exception as e:
        return("false")
    return(id)

@app.route('/showType', methods=['get']) #查询所有联系人类型
def showType():
    res = newBPrelationship.searchallRelationshipDic()
    return(jsonify(res))

@app.route('/searchBP1', methods=['post']) # 按条件查询客户
def searchBP1():
    searchTerm = request.get_json()
    res = newBPrelationship.searchCustomer(POcode=searchTerm['POcode'],city=searchTerm['city'],country=searchTerm['country'],postcode=searchTerm['postcode'],name=searchTerm['name'])
    return(jsonify(res))

@app.route('/searchBP2', methods=['post']) # 按条件查询联系人
def searchBP2():
    searchTerm = request.get_json()
    res = newBPrelationship.searchContactPerson(POcode=searchTerm['POcode'],last_name=searchTerm['last_name'],first_name=searchTerm['first_name'])
    return(jsonify(res))

@app.route('/showWarehouse', methods=['get']) #查询所有仓库信息
def showWarehouse():
    res = newWarehouseManager.searchallWarehouse()
    return(jsonify(res))

@app.route('/showMaterialDic', methods=['get']) #查询所有物料词条
def showMaterialDic():
    res = newWarehouseManager.searchallMaterialDic()
    return(jsonify(res))

# @app.route('/searchPrice', methods=['post']) # 查询对应物料的价格
# def searchPrice():
#     id = request.get_json()
#     res = newWarehouseManager.searchPrice(id['material'])
#     print("查询结果是",res[0])
#     return(jsonify(res[0]))

@app.route('/createInquiry', methods=['post']) # 创建询价单及询价单物料项
def createInquiry():
    a = request.get_json()[0]
    b = request.get_json()[1]
    a['PODate'] = datetime.strptime(a['PODate'],'%Y-%m-%d')
    a['effectiveDate'] = datetime.strptime(a['effectiveDate'],'%Y-%m-%d')
    a['expirationDate'] = datetime.strptime(a['expirationDate'],'%Y-%m-%d')
    try:
        id = newOrderManager.insertInquiry(a)
        for item in b:
            item['inquiryId'] = id # 把询价单编号加进询价单物料项的词条
            del item['price']
            newOrderManager.insertInquiryItem(item)
    except Exception as e:
        return("false")
    return(id)

@app.route('/showDiscountDic', methods=['get']) #查询所有物料词条
def showDiscountDic():
    res = newOrderManager.searchallDiscountDic()
    return(jsonify(res))

@app.route('/createQuotation', methods=['post']) # 创建询价单及询价单物料项
def createQuotation():
    a = request.get_json()[0]
    b = request.get_json()[1]
    a['PODate'] = datetime.strptime(a['PODate'],'%Y-%m-%d')
    a['effectiveDate'] = datetime.strptime(a['effectiveDate'],'%Y-%m-%d')
    a['expirationDate'] = datetime.strptime(a['expirationDate'],'%Y-%m-%d')
    a['requestedDeliveryDate'] = datetime.strptime(a['requestedDeliveryDate'],'%Y-%m-%d')
    try:
        id = newOrderManager.insertQuotation(a)
        for item in b:
            item['quotationId'] = id # 把报价单编号加进报价单物料项的词条
            del item['price']
            newOrderManager.insertQuotationItem(item)
    except Exception as e:
        return("false")
    return(id)

if __name__ == '__main__':
    app.run()