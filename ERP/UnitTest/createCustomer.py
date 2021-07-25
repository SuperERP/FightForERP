from ERP.Modules.SuperErp import *

newCustomer = CustomerManagerModule(session, ErpLogger)
nc={}
nc['name']='zht'
nc['street']="sp"
nc['postcode']="111"
nc['country']="CN"
nc['language']="CH"
nc['accountantId']="1853245"
nc['paycode']="1853245"
nc['distribution_channel']="00"
nc['distribution_area']="CN00"
nc['sales_channel_number']="0"
nc['POcode']="123"
newCustomer.insertCustomer(nc)
