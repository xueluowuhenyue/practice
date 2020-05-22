from API_D.Common.public.read_ini import configuration
from API_D.Common.public import project_path
import re
class getdata:
    '''可以用来动态的更改 删除 获取数据'''
    cookies=''
    NUM=''            #标ID
    YUE=''             #提现前的余额
    MONEY=''           #充值前的余额

    mobilephone=configuration(project_path.config_path).read_str('data','mobilephone')
    password=configuration(project_path.config_path).read_str('data','password')
    memberid=configuration(project_path.config_path).read_str('data','memberid')
    url=configuration(project_path.config_path).read_str('URL','url')

def replace(str):
    '''这是一个用来查询替换的函数，str传入的字符串'''
    p='#(.*?)#'
    '''P替换的规则'''
    while re.search(p,str):
        '''获取需要替换的字符串'''
        key=re.search(p,str).group(1)
        '''关联反射'''
        value = getattr(getdata,key)
        '''替换查询到的字符'''
        str=re.sub(p,value,str,count=1)
    return str


if __name__ == '__main__':
    replace("{'mobilephone':'#mobilephone#','password':'#password#','memberid':'#memberid#'}")
    "#url#/futureloan/mvc/api/member/register"

#类属性
# print(GetData.COOKIE)
# print(GetData().COOKIE)
#类的反射可以动态的查看，增加，删除，更改类里面的属性
#利用反射的方法来拿值
# print(getattr(GetData,'COOKIE'))#第一个参数是类名  第二个参数是属性的参数名
# print(hasattr(GetData,'COOKIE'))#第一个参数是类名  第二个参数是属性的参数名 返回值是布尔值
# print(setattr(GetData,'COOKIE','123456'))
# #第一个参数是类名  第二个参数是属性的参数名 第三个你要设置的新值
# print(getattr(GetData,'COOKIE'))
#
# print(delattr(GetData,'COOKIE'))#删除类的某个属性  #第一个参数是类名  第二个参数是属性的参数名
# #不常用
# print(getattr(GetData,'COOKIE'))