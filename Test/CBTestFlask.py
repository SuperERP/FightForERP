import sys

new_path = "/".join(sys.path[0].split('/')[:-1])
sys.path.append(new_path)

from ERP.Modules.SuperErp import *
import time
import os
from datetime import date
from flask import jsonify
from ERP.Modules.WarehouseManager import WareHouseDataManager
from flask import Flask, request
from flask_cors import CORS


newCustomer = CustomerManagerModule(session, ErpLogger)

newDelivery = DeliveryManagerModule(session, ErpLogger)
newOrder = OrderManagerModule(session, ErpLogger)
newware = WareHouseDataManager(session, ErpLogger)

# 实例化产生一个Flask对象

app = Flask(__name__)
CORS(app, supports_credentials=True)


# flask的路由是基于装饰器的
@app.route('/fuck', methods=['post'])
def hello_world():
    data = newDelivery.searchallDelivery()
    print(data)
    ret = {}
    ret['data'] = data
    return jsonify(ret)


if __name__ == '__main__':

    app.run()
