import logging
from logmodule.readconf import configfile


class MyLog:
    """这是一个日志类"""
    def __init__(self,filename=None, inputlevel=None, outlevel=None, formatter=None):
        self.filename=configfile('log.ini').readfile('LOG','filename')
        self.inputlevel=configfile('log.ini').readfile('LOG','inputlevel')
        self.outlevel=configfile('log.ini').readfile('LOG','outlevel')
        self.formatter=configfile('log.ini').readfile('LOG','formatter')

    def my_log(self, level, msg):
        # 创建日志收集器
        my_log=logging.getLogger(self.filename)
        # 设置收集日志的级别
        my_log.setLevel(self.inputlevel)

        formatter = logging.Formatter(self.formatter)
        # 控制台输出
        ch=logging.StreamHandler()
        # 设置日志输出级别
        ch.setLevel(self.outlevel)
        # 定义日志输出格式
        ch.setFormatter(formatter)
        # 日志记录
        fh=logging.FileHandler(self.filename,encoding='utf-8')
        # 设置日志输出级别
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        # 日志关联
        my_log.addHandler(fh)
        my_log.addHandler(ch)

        if level=='DEBUG':
            my_log.debug(msg)
        elif level == 'INFO':
            my_log.info(msg)
        elif level == 'WARNING':
            my_log.warning(msg)
        elif level == 'ERROR':
            my_log.error(msg)
        else:
            my_log.critical(msg)

        # 断开连接
        my_log.removeHandler(ch)
        my_log.removeHandler(fh)

    def debug(self,msg):
        self.my_log('DEBUG',msg)

    def info(self,msg):
        self.my_log('INFO',msg)

    def warning(self,msg):
        self.my_log('WARNING',msg)

    def error(self, msg):
        self.my_log('ERROR', msg)

    def critical(self, msg):
        self.my_log('CRITICAL', msg)


if __name__ == '__main__':
    p=MyLog()
    p.info('fdhgj')
    p.error('睡觉啦！！！')
    p.warning('poiuyt')
    p.error('88888')
    p.critical('kkkkkk')