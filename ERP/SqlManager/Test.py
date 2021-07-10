from WareHouse import *
from CustomerData import *
from DeliveryData import *
from InquiryData import *
from QutationData import *

Base.metadata.create_all()  # 将模型映射到数据库中
data = {'id': 'fuck', 'name': 'fasd', ' price': 'adsf'}
session.add_all([
    MaterialDic(id='fuck', name='das', price=19.0)

])

session.commit()