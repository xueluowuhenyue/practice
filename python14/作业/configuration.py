# -*- coding:utf-8 -*-
# 写一个配置类 有以下几个函数：
#1：读取整数
#2：读取浮点数
#3：读取布尔值
#4：读取其他类型的数据 list tuple dict eval（）
#5：读取字符串
from configparser import ConfigParser
class configuration:
    def __init__(self,file_name):
        self.cf=ConfigParser()
        self.cf.read(file_name,encoding='utf-8')
    def read_int(self,section,option):
        '''读取整数'''
        value=self.cf.getint(section,option)
        return value
    def read_bool(self,section,option):
        '''读取布尔值'''
        value=self.cf.getboolean(section,option)
        return value
    def read_float(self,section,option):
        '''读取浮点数'''
        value=self.cf.getfloat(section,option)
        return value
    def read_str(self,section,option):
        '''读取字符串'''
        value=self.cf.get(section,option)
        return value
    def read_else(self,section,option):
        '''读取其他数据类型'''
        value=self.cf.get(section,option)
        return eval(value)
if __name__ == '__main__':
    p=configuration('D:\pycharm\python14\week6\py14.ini')
    p.read_int('py14StudentName','name_2')
    p.read_float('py14StudentName','name_3')
    p.read_bool('py14StudentName','name_4')
    p.read_else('py14StudentName','name_7')
    p.read_str('py14StudentName','name_5')
    print(p.read_str('py14StudentName','name_5'))


