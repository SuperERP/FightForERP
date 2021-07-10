from ERP.SqlManager.BaseUtil import *



class User(Base):
    __tablename__ = 'User'
    id = Column(String(10), primary_key=True)
    passWord = Column(String(10), nullable=False)
