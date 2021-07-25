class AbstractModule:
    def __init__(self, session, logging):
        self.session = session
        self.logging = logging
        pass

    def getTimeId(self):
        '''
        获取时间戳标记id
        :return:
        '''
        import time
        return time.strftime("%Y%H%M%S%m%d", time.localtime())

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
            self.logging.info('success insert data %s' % (str(ormData)))
        except Exception as e:
            ans = False
            self.logging.info('请重新检查数据插入')

            self.logging.error(e)
            self.session.rollback()

        return ans
