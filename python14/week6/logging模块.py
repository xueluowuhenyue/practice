# -*- coding:utf-8 -*-
import logging
class Mylog:
    def mylog(self,level,msg):
        my_logger=logging.getLogger('python14')
        my_logger.setLevel('DEBUG')

        formatter = logging.Formatter('[%(asctime)s]-[%(levelname)s]-[日志信息]:%(message)s')
        # ch=logging.StreamHandler()
        # ch.setLevel('INFO')#设置级别
        # ch.setFormatter(formatter)#设置格式

        fh=logging.FileHandler('test.log',encoding='utf-8')
        fh.setLevel('INFO')#设置级别
        fh.setFormatter(formatter)#设置格式

        # my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical('this is critical msg')

        my_logger.removeHandler(fh)#fh ch
        # my_logger.removeHandler(ch)#一定要记得移除掉

    def info(self,msg):
        self. mylog('INFO',msg)
    def warning(self,msg):
        self. mylog('WARNING',msg)
    def error(self,msg):
        self. mylog('ERROR',msg)
    def critical(self,msg):
        self. mylog('CRITICAL',msg)

p=Mylog()
p.error('停电了')