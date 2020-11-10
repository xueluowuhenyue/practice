# -*- coding:utf-8 -*-
import os
import time
new = time.strftime('%Y-%m-%d')
log_name = new+'.txt'

path = os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]
# path= os.path.realpath(__file__)
print(path)

Log_path=os.path.join(path, 'Result', 'Log', log_name)
# print(Log_path)
Conf_path=os.path.join(path, 'Common', 'Conf', 'conf.ini')
# print(Conf_path)
Excel_path=os.path.join(path, 'Data', 'Login.xlsx')
# print(Excel_path)