# -*- coding:utf-8 -*-
from configparser import ConfigParser
from Common.Public import project_path
class configuration:
    def __init__(self,file_name):
        self.cf=ConfigParser()
        self.cf.read(file_name,encoding='utf-8')

    def read_str(self,section,option):
        '''读取字符串'''
        value=self.cf.get(section,option)
        return value
    def read_else(self,section,option):
        '''读取其他数据类型'''
        value=self.cf.get(section,option)
        return eval(value)
if __name__ == '__main__':
    p=configuration(project_path.config_path)
    print(project_path.config_path)
    print(p.read_str('DATA','mobilephone'))
