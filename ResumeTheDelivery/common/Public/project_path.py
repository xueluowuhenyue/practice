# -*- coding:utf-8 -*-
import  os
import time
path=os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]
new=time.strftime('%Y-%m-%d')
time_path=new+'.txt'
img_name=new+'.png'
# 日志路径
log_path=os.path.join(path,'Result','log',time_path)
# print(log_path)

# 测试报告路径
report_path=os.path.join(path,'Result','report','APP_test.html')


# 配置文件路径
config_path=os.path.join(path,'common','Conf','conf.ini')
# print(config_path)

# Excel表格路径
Excel_path=os.path.join(path, 'data', 'job.xlsx')
# print(Excel_path)
# 图片路径
picture_path=os.path.join(path, 'Result', 'Img', img_name)