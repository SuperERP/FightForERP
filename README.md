##  前端配置

1. 安装[node.js](https://cloud.tencent.com/developer/article/1631257)
2. 安装[cnpm](https://www.cnblogs.com/uniapp/p/13115877.html)

（1和2建议通过控制台安装在C盘）通过控制台进入项目的前端文件夹(Front)，运行以下语句就能够运行前端程序

```sh
cnpm install
cnpm run serve
```

## 后端配置

1. 安装[python](https://blog.csdn.net/weixin_37424315/article/details/89929650)环境
2. 使用[pip](https://www.runoob.com/w3cnote/python-pip-install-usage.html)工具安装
   + sqlalchemy
   + flask
   + colorlog
   + flask_cors

##  启动项目

1. 在项目的前端文件夹(Front)下通过控制台运行以下语句就能够启动前端程序

   ```sh
   cnpm install
   cnpm run serve
   ```


   2.后端运行ERP/Zhtest文件夹中的Flask_allpart.py

   3.在浏览器输入网址http://localhost:8080/Logon

​      进入登录界面，登录即可，后续操作请参考Report文件夹中系统设计报告“用户界面设计说明”。

​       可用用户如下（建议登录SuperManager，可使用所有功能模块）：

| ***id\***       | password        | power |
| --------------- | --------------- | ----- |
| SuperManager    | FightForERP     | 10    |
| SalesMember     | salesmember     | 1     |
| SalesManager    | salesmanager    | 2     |
| WarehouseKeeper | warehousekeeper | 3     |



