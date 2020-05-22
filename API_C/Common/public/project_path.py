# -*- coding:utf-8 -*-
import  os
import time
path=os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]
#日志路径
new=time.strftime('%Y-%m-%d')
time_path=new+'.txt'
log_path=os.path.join(path,'Result','test_log',time_path)

#测试报告路径
report_path=os.path.join(path,'Result','test_report','test.html')
# print(report_path)

#配置文件路径
config_path=os.path.join(path,'Common','conf','case_option.ini')

#Excel路径
excel_path=os.path.join(path,'Test_data','data','data.xlsx')
print(excel_path)