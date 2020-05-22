# -*- coding:utf-8 -*-
#for循环：有限次数循环
#for循环的作用： 1.遍历元素 2.控制循环次数
#for循环遍历的数据类型：str tuple list dict 循环的次数有元素的长度决定
# d={'name':'ki','age':18,'sal':'20k'}
# a=0
# for i in d.keys():
#     a+=1
#   print('这是第{}次循环',format(a))
#     print(i)
#     print()#换行
#range函数：生成一个整数序列 可迭代对象
#range(m:n:k)#m开始的数字，n结尾的数字，k步长 取左不取右
#如果range（m，n）默认k=1
#如果range（m）从0开始
# res=range(1,10)
# print(set(res))
# res=range(10)
# print(set(res))
#生成0-100的数字
# res=range(0,101)
# print(list(res))
# for i in range(101):
#     print(i)
#写0-100的数字奇数、偶数和
# sum_1=0
# for i in range(1,101,2):
#     sum_1=sum_1+i
# print(sum_1)
# sum_2=0
# for i in range(0,101,2):
#     sum_2=sum_2+i
# print(sum_2)
# sum_1=0#初始值奇数和
# sum_2=0#初始值偶数和
# for i in range(0,101):
#     if i%2==0:
#         sum_2=sum_2+i
#     if i%2 !=0:
#         sum_1=sum_1+i
# print('奇数和：',sum_1)
# print('偶数和：',sum_2)
#嵌套循环 循环中还有循环
# p=[[1,2,3],[4,5,6],[7,8,9]]
# for i in p:#外层循环
#     for b in i:#内层循环
#         print(b)
#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%2d" % (j,i,j*i),end=' ')
#     print(" ")
# s='python'
# a=0
# for i in s:
#     a+=1#赋值运算
#     print('{}歌名 离殇'.format(a))
#     print('------')
# d={'name':'hk','age':18,'height':170.52,'hobby':'钓鱼'}
# for i in d.values():
#     print(i)
p=[[1,2,3],[4,5,6],[7,8,9]]
for i in p:
    for f in i:
        print(f,end=' , ')