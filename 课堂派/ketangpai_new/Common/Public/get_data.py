# -*- coding:utf-8 -*-
from Common.Public import project_path
from Common.Public.read_conf import configuration
import re
class GetData:
    # username=configuration(project_path.config_path).read_str('DATA','username')
    password=configuration(project_path.config_path).read_str('DATA','password')
    code=configuration(project_path.config_path).read_str('DATA','code')
    grade=configuration(project_path.config_path).read_str('DATA','grade')
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

if __name__ == '__main__':
    GetData()
    # replace("{'client_ip':'192.168.1.225','tmpl_id':1,'mobile':'1369654123'}")  #{' mobile':'#mobile#','url':'#url#'}

