from flask import Flask
# 实例化产生一个Flask对象
app = Flask(__name__)

#flask的路由是基于装饰器的
@app.route('/') 
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()      # 看源码发现，最终调用了werkzeug的run_simple()