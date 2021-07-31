class AbstractModule:
    def __init__(self, session, logging):
        self.session = session
        self.logging = logging
        pass

    def to_dict(self,data):
        return {c.name: getattr(data, c.name, None) for c in data.__table__.columns}




    def getTimeId(self):
        '''
        获取时间戳标记id
        :return:
        '''
        import datetime
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')

    def str_to_date(self, dateStr):
        '''

        :param dateStr:
        :return:
        '''
        import datetime
        from dateutil import parser
        return parser.parse(dateStr).date()



    def insertData(self, ormData):
        ans = True
        try:
            self.session.add(ormData)
            self.session.commit()
            self.logging.info('success insert data %s' % (str(ormData)))
        except Exception as e:
            ans = False
            self.logging.info('请重新检查数据插入')

            self.logging.error(e)
            self.session.rollback()

        return ans
