# -*- coding:utf-8 -*-
#1.利用while循环 完成1-100的整数数字相加和
# num=0  #初始值为0
# a=0    #从0开始
# while a<100:
#     a+=1
#     num+=a    #累加
# print(num)

#2.利用for循环 完成1-10的整数数字相加和
# num=0    #初始值为0
# for i in range(1,11):
#     num+=i
# print(num)

# 3：利用for循环输出如下三角形
#
# *
#
# **
#
# ***
#
# ****
#
# *****

# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()

#4：请用嵌套for循环输出如下等边三角形（三个边均为5个*）
#       *
#
#      *  *
#
#    *  *   *
#
#   *  *  *  *
#
# *  * *  *  *  *

# for i in range(1,6):
#     for k in range(1,6-i):
#         print(" ",end='')
#     for j in range(1,i+1):
#         print('* ',end='')
#     print()

#5:输出99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d'% (j,i,i*j), end=' ')
#     print()

#6:利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序
# a=[1,7,4,89,34,2]
# for i in range(len(a)-1):
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             m=a[j]                        #位置交换
#             a[j]=a[j+1]
#             a[j+1]=m
# print(a)

#7:有1 2 3 4 这四个数字，能组成多少个互不相同且无重复数字的三位数？分别是什么？
# count=0    #初始次数为0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if  i!=j and j!=k and i!=k:  #规定三个数必须唯一
#                 print(i,j,k)
#                 count+=1                  #每增加一个数次数加1
# print(count)

#8:求 0—7 所能组成的奇数个数
# count=1                   #初始值为1
# sum=0                     #初始个数为0
# for i in range(0,8):
#     if i==0:              #一位数的奇数个数
#         count=4*1
#     elif i==1:            #两位数的奇数个数
#         count=4*7
#     else:
#         count *=8         #大于两位的奇数个数
#     sum=sum+count         #累加生成奇数的个数
# print(sum)

#9:购物车程序 需求
# d={'num':{1:{'苹果':'4元'},2:{'葡萄':'6元'},3:{'草莓':'40元'},4:{'菠萝':'11元'}}}
# #1：启动程序后，让用户在控制台输入工资，然后打印商品信息（随便你们自己用什么方式存储商品，记得要有商品的编号、名称以及价格）
# print(d['num'])
# for i in d['num'].keys():                                          #获取商品编号
#     for name in d['num'][i].keys():                                #获取商品名称
#         print('''
#                 商品编号{}
#                 商品名称：{}
#                 商品价格：{}'''.format(i,name,d['num'][i][name]))      #根据名称取价格


# 2：允许用户根据商品编号购买商品
#
# 3：用户选择商品后，监测余额是否足够，如果足够就直接扣款，不够就提醒用户，不能购买这个商品。
#
# 4：可随时退出，退出后，打印已购买商品和余额