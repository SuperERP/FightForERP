from WareHouse import *
from CustomerData import *
from DeliveryData import *
from InquiryData import *
from QutationData import *
from ErpLoggin import *
import traceback

Base.metadata.create_all()  # 将模型映射到数据库中
data = {'id': 'fuck', 'name': 'data', 'price': 190}
# session.add(
#     MaterialDic(data),
# )
# print(**data)
print(MaterialDic(**data))

# session.add(
#     MaterialDic(id='fuck', name='das', price=19.0),
# )
#
# try:
#     session.add(
#         MaterialDic(id='fuck', name='das', price=19.0),
#     )
#     session.commit()
# except Exception as e:
#     print(e.args)
#     ErpLogger.error(e)
#     session.rollback()
# finally:
#     print('asdfasdf')

# session.close()  # optional, depends on use case

session.commit()
