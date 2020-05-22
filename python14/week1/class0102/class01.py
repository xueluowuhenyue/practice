# -*- coding:utf-8 -*-
# print('8888\n',888)
# #字符串反序
# s='cxbvcxnvbzmx,cvmz,'
# print(s[-1::-1])
# name='ha'
# age=18
# height=170.21
# hobby='钓鱼'
# print('''
#     我是:{}
#     年龄:{}
#     身高:{}
#     爱好:{}'''.format(name,age,height,hobby))
#字符串拼接
# s='vjbnkcnb'
# print(','.join(s))

# d={'name':'ff','age':18,'sex':'f'}
#
# def read(*args):
#     print(*args)
#     print(args)
# read({'a':{'name':'ff','age':18,'sex':'f'}})

# l=[5,9,8,2,0,4,6,7,5.2]
# l.pop()         #从最后开始删除
# l.remove()     #删除整数
# l[2]=1          #修改
# l.reverse()      #倒序
# print(l)
# a=sorted(l)    #从小到大
# print(a)
# print(sorted(l,reverse=True))   #从大到小

# 给你一个字典a={1:1,2:2,3:3}，输出字典a的key，以','连接，如'1,2,3'. join
# a={1:1,2:2,3:3}
# m = list(a.keys())
# n = []
# for i in m:
#     n.append(str(i))
# print(','.join(n))

s='vcbmxvcnb,cv'
m=''
for i in s:
    m+=i
    m+='、'
print(m)