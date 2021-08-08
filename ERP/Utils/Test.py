from ERP.Modules.OrmData.WareHouse import *
import datetime
from dateutil import parser

dateStr = ' 5 6 2011'
print(parser.parse(dateStr).date())
Base.metadata.create_all()  # 将模型映射到数据库中
# def
# 法1
# 法2

session.add(
    MaterialDic(id='fuck', name='das', price=19.0),
)

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
