from flask import Flask, request
# 实例化产生一个Flask对象
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


# flask的路由是基于装饰器的
@app.route('/fuck', methods=['post'])
def hello_world():
    print('dfasd')
    data = request.get_json(silent=True)
    print(type(data))
    # 这个东西是一个字典

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
