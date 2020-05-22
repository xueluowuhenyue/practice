# -*- coding:utf-8 -*-
from configparser import ConfigParser
from Common.Public import Project_path


class DyConf:
    def __init__(self, file_name):
        self.cf = ConfigParser()
        self.cf.read(file_name, encoding='utf-8')

    def read_str(self, section, option):
        value = self.cf.get(section, option)
        return value

    def read_else(self, section, option):
        value = self.cf.get(section, option)
        return eval(value)


if __name__ == '__main__':
    res=DyConf(Project_path.Conf_path).read_str('LOG','logger_name')
    print(res)