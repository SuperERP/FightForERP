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

newContactPerson = CustomerManagerModule(session, ErpLogger)

# 实例化产生一个Flask对象
app = Flask(__name__)
CORS(app, supports_credentials=True)

# flask的路由是基于装饰器的
@app.route('/createContactPerson', methods=['post'])
def createContactPerson():
    a = request.get_json()
    # print(a)
    try:
        id = newContactPerson.insertContactPerson(a)
    except Exception as e:
        return("false")
    return(id)

if __name__ == '__main__':
    app.run()