# -*- coding:utf-8 -*-
from WebService.Common.Public import project_path
from WebService.Common.Public.read_conf import configuration
import time,datetime
import re
class GetData:
    mobile=configuration(project_path.config_path).read_str('DATA','mobile')
    pwd=configuration(project_path.config_path).read_str('DATA','pwd')
    url=configuration(project_path.config_path).read_str('DATA','url')
    num=str(int(mobile[-2])*10+int(mobile[-1])*1)            #获取数据库名
    nu=mobile[-3]
def replace(str):
    p='#(.*?)#'
    '''P替换的规则'''
    while re.search(p,str):
        '''获取需要替换的字符串'''
        key=re.search(p,str).group(1)
        '''关联反射'''
        value = getattr(GetData,key)
        '''替换查询到的字符'''
        str=re.sub(p,value,str,count=1)

    return str

# if __name__ == '__main__':
    # replace("{'client_ip':'192.168.1.225','tmpl_id':1,'mobile':'1369654123'}")  #{' mobile':'#mobile#','url':'#url#'}

