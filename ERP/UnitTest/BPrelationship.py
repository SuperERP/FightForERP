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

newBPrelationship = CustomerManagerModule(session, ErpLogger)

# 实例化产生一个Flask对象
app = Flask(__name__)
CORS(app, supports_credentials=True)

# flask的路由是基于装饰器的
@app.route('/createBPrelationship', methods=['post'])
def createBPrelationship():
    a = request.get_json()
    a['validTo'] = datetime.strptime(a['validTo'],'%Y-%m-%d')
    a['validFrom'] = datetime.strptime(a['validFrom'],'%Y-%m-%d')
    id = newBPrelationship.insertCustomerAndContactPersonRelationship(a)
    return(id)

@app.route('/showType', methods=['get'])
def showType():
    res = newBPrelationship.searchallRelationshipDic()
    return(jsonify(res))

@app.route('/searchBP1', methods=['post'])
def searchBP1():
    searchTerm = request.get_json()
    res = newBPrelationship.searchCustomer(POcode=searchTerm['POcode'],city=searchTerm['city'],country=searchTerm['country'],postcode=searchTerm['postcode'],name=searchTerm['name'])
    return(jsonify(res))

@app.route('/searchBP2', methods=['post'])
def searchBP2():
    searchTerm = request.get_json()
    res = newBPrelationship.searchContactPerson(POcode=searchTerm['POcode'],last_name=searchTerm['last_name'],first_name=searchTerm['first_name'])
    return(jsonify(res))

if __name__ == '__main__':
    app.run()