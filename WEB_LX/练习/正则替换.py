# -*- coding:utf-8 -*-
from API_D.Common.public.GETDATA import getdata
import re
dict="{'mobilephone':'#mobilephone#','password':'#password#'}"
p='#(.*?)#'

# m=re.search(p,d).group(1)
# print(m)
while re.search(p,dict):
    key=re.search(p,dict).group(1)
    value = getattr(getdata,key)
    dict=re.sub(p,value,dict,count=1)
print(dict)