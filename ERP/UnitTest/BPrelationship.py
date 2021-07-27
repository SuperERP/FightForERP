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

newBPrelationshiup = CustomerManagerModule(session, ErpLogger)

# 实例化产生一个Flask对象
app = Flask(__name__)
CORS(app, supports_credentials=True)

# flask的路由是基于装饰器的
@app.route('/createBPrelationship', methods=['post'])
def createBPrelationship():
    a = request.get_json()
    a['validTo'] = datetime.strptime(a['validTo'],'%Y-%m-%d')
    a['validFrom'] = datetime.strptime(a['validFrom'],'%Y-%m-%d')
    id = newBPrelationshiup.insertCustomerAndContactPersonRelationship(a)
    return(id)

@app.route('/showType', methods=['get'])
def showType():
    print("testttt")
    res = []
    res = newBPrelationshiup.searchallRelationshipDic()
    return(res)

if __name__ == '__main__':
    app.run()