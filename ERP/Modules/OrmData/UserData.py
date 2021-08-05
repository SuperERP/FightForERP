from .BaseUtil import *

class User(Base):
    __tablename__ = 'User'
    id = Column(String(10), primary_key=True)
    password = Column(String(10), nullable=False)
    power = Column(Float, ForeignKey('Power.level'))

    def __init__(self, **data):
        self.id = data['id']
        self.password = data['password']
        self.power = data['power']

class Power(Base):
    __tablename__ = 'Power'
    level = Column(Float)
    content = Column(String(50), nullable=False)
    __table_args__ = (
         PrimaryKeyConstraint('level', 'content'),
    )
    def __init__(self, **data):
        self.level = data['level']
        self.content = data['content']