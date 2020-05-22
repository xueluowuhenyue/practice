# -*- coding:utf-8 -*-
import pandas as pd
#打开文件
df=pd.read_excel('py14.xlsx')
#获取所有值
res=df.values
#打印结果
print(res)

