from .AbstractModule import *
from .OrmData.UserData import *

class UserManagerModule(AbstractModule):
    def __init__(self, session, logging):
        '''
        :param session:
        :param idrecord:
        :param logging:
        '''
        super().__init__(session, logging)
    
    def login(self, id, password):
        Base.metadata.create_all()
        res=[]
        for idata in self.session.query(User).filter(User.id==id).filter(User.password==password).all():
            res.append(self.to_dict(idata))
        if res == []:
            return "fault"
        else:
            return "success"

    def changePasswd(self, id, password, newPassword):
        try:
            if self.login(id=id, password=password)=="success":
                self.session.query(User).filter(User.id==id).update({"password":newPassword})
                self.session.commit()
            else:
                return "fault"
        except Exception as e:
            self.logging.info('请重新检查数据修改')
            self.logging.error(e)
            self.session.rollback()
            return "fault"
        return "success"