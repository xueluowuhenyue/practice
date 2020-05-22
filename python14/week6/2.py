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
        self.file_name=file_name
    def read_int(self,section,option):
        '''读取整数'''
        # #创建对象
        cf=ConfigParser()
        #打开文件
        cf.read(self.file_name,encoding='utf-8')
        # #读取内容
        res=cf.getint(section,option)
        print(res)
    def read_bool(self,section,option):
        '''读取布尔值'''
        cf=ConfigParser()
        #打开文件
        cf.read(self.file_name,encoding='utf-8')
        # #读取内容
        res=cf.getboolean(section,option)
        print(res)
    def read_float(self,section,option):
        '''读取浮点数'''
        cf=ConfigParser()
        #打开文件
        cf.read(self.file_name,encoding='utf-8')
        # #读取内容
        res=cf.getfloat(section,option)
        print(res)
    def read_str(self,section,option):
        '''读取字符串'''
        cf=ConfigParser()
        #打开文件
        cf.read(self.file_name,encoding='utf-8')
        # #读取内容
        res=cf.get(section,option)
        print(res)
    def read_else(self,section,option):
        '''读取其他数据类型'''
        cf=ConfigParser()
        #打开文件
        cf.read(self.file_name,encoding='utf-8')
        # #读取内容
        res=cf.get(section,option)
        print(res)
p=configuration('py14.ini')
p.read_int('py14StudentName','name_2')
p.read_float('py14StudentName','name_3')
p.read_bool('py14StudentName','name_4')
p.read_else('py14StudentName','name_7')
p.read_str('py14StudentName','name_5')
# #创建对象
# cf=ConfigParser()
# #打开文件
# cf.read('py14.ini',encoding='utf-8')
# #读取内容
# res=cf.get('py14StudentName','name_6')
# if type(eval(res))==list:        #判断列表
#     print(666)
# else:
#     print(111)
#打印结果
# print(res)
# print(type(res))
# print(type(eval(res)))


