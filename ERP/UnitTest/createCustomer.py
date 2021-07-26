import sys

new_path = "/".join(sys.path[0].split('/')[:-1])
sys.path.append(new_path)

from ERP.Modules.SuperErp import *
import time
import os
from datetime import date
from flask import jsonify
from flask import Flask, request
from flask_cors import CORS

newCustomer = CustomerManagerModule(session, ErpLogger)

# 实例化产生一个Flask对象
app = Flask(__name__)
CORS(app, supports_credentials=True)

# flask的路由是基于装饰器的
@app.route('/createCustomer', methods=['post'])
def createCustomer():
    a = request.get_json()
    id = newCustomer.insertCustomer(a)
    return(id)

if __name__ == '__main__':
    app.run()