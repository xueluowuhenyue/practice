# -*- coding:utf-8 -*-
# Python3基础11——打印三角形
# 例1：请利用嵌套for循环生成一个直角三角形图形
# *
# **
# ***
# ****
# *****
# 1 for i in range(1,6):
# 2     for j in range(0,i):
# 3         print("*",end="")
# 4     # 占位让程序换行
# 5     print()
# 思路：总共有5行，就用range(1,6)，发现第N行就有N个“*”，每一行的“*”就用range(1,N)来表示，print默认输出是换行的，要想实现不换行则需在末尾加上end = " "，每一行循环完毕就用print()输出换行
#
# 不用嵌套循环实现：

#  1 for i in range(1,6):
#  2     # 第i行就打印i个“*”
#  3     print("*"*i,end="")
#  4     print()
#  5
#  6 *
#  7 **
#  8 ***
#  9 ****
# 10 *****

# 例2：输出等边三角形（三条边均为5个*）
#
#  1 for Index_row in range(1,6):
#  2     # 打印每一行前面的空格
#  3     for index_space in range(1,6-Index_row):
#  4         print(" ",end="")
#  5     # 打印“* ”
#  6     for Index_col in range(1,Index_row+1):
#  7         print("* ",end="")
#  8     print()
#  9
# 10     *
# 11    * *
# 12   * * *
# 13  * * * *
# 14 * * * * *

# 思路：总共有5行，就用range(1,6)，发现第N行就有N个“* ”+（6-N-1）（PS：若从1开始不是0开始的就是6-N）个空格，每一行的“* ”就用range(1,N+1)来表示，print默认输出是换行的，要想实现不换行则需在末尾加上end = " "，每一行循环完毕就用print()输出换行
#
# 例3：打印等腰三角形（答案同例1）
#
# 例4：打印倒三角形

#  1 for i in range(1,6):
#  2     for j in range(6-i,0,-1):
#  3         print("*",end="")
#  4     print()
#  5
#  6 *****
#  7 ****
#  8 ***
#  9 **
# 10 *


# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 2018年10月03日 19:49:01 小代码大用处 阅读数：83
# #answer 1
# input_para=[1,2,3,4]
# l=0 #计数
# for i in input_para:
#     for j in input_para:
#         for k in input_para:
#             if(i!=j and i!=k and j!=k):
#                 l+=1
#                 print(i,j,k)
# print(l)

#求 0—7 所能组成的奇数个数
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

#利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序
# a=[1,7,4,89,34,2]
# for i in range(len(a)-1):
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             m=a[j]                        #位置交换
#             a[j]=a[j+1]
#             a[j+1]=m
# print(a)

#有1 2 3 4 这四个数字，能组成多少个互不相同且无重复数字的三位数？分别是什么？
# count=0    #初始次数为0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if  i!=j and j!=k and i!=k:  #规定三个数必须唯一
#                 print(i,j,k)
#                 count+=1                  #每增加一个数次数加1
# print(count)

# -*- coding:utf-8 -*-
# 1.利用while循环 完成1-100的整数数字相加和
# c=0
# sum=0
# while True:
#     c+=1
#     sum+=c
#     if c==100:
#         break
# print(sum)

# 2.利用for循环 完成1-10的整数数字相加和
# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)

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
# for i in range(1,6):                   #层数
#     for j in range(1,i+1):             #每层数量
#         print('*',end='')
#     print()
#解法二
# for i in range(1,6):
#     print('*'*i,end='')    #*个数等于循环次数
#     print()

# 4：请用嵌套for循环输出如下等边三角形（三个边均为5个*）
#
#        *
#
#      *  *
#
#    *  *   *
#
#   *  *  *  *
#
# *  * *  *  *  *
# for i in range(1,6):            #层数
#     for j in range(1,6-i):      #空格数
#         print(' ',end='')       #格式
#     for k in range(1,i+1):      #*数量
#         print('*',end=' ')
#     print()

# 5:输出99乘法表
# for i in range(1,10):                                    #左下
#     for j in range(1,i+1):
#         print('%s*%s=%s'%(j,i,i*j),end=' ')
#     print()
# for i in range(1,10):                                     #右下
#     for j in range(1,10-i+1):
#         print('%s*%s=%2s'%(j,i,i*j),end=' ')
#     print()

# 6:利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序：
# a=[1,7,4,89,34,2]
# for i in range(len(a)-1):                   #循环次数
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:                     #位置交换
#             k=a[j]
#             a[j]=a[j+1]
#             a[j+1]=k
# print(a)
# 冒泡排序：小的排前面，大的排后面。
#
#
# 7:有1 2 3 4 这四个数字，能组成多少个互不相同且无重复数字的三位数？分别是什么？
# count=0
# for i in range(1,5):                                 #第一个数
#     for j in range(1,5):                              #第二个数
#         for k in range(1,5):                           #第三个数
#             if i !=j and j !=k and k !=i:
#                 print(i,j,k)
#                 count+=1
# print(count)

#
# 8:求 0—7 所能组成的奇数个数
# cuont=1
# sum=0   #初始次数为0
# for i in range(8):          #最大八位数
#     if i==0:                #一位数的奇数个数
#         count=4*1
#     elif i==1:              #两位数的奇数个数
#         count=4*7
#     else:
#         count*=8
#     sum+=count
# print(sum)

# 9:购物车程序 需求：
#
# 1：启动程序后，让用户在控制台输入工资，然后打印商品信息（随便你们自己用什么方式存储商品，记得要有商品的编号、名称以及价格）
# 2：允许用户根据商品编号购买商品
# 3：用户选择商品后，监测余额是否足够，如果足够就直接扣款，不够就提醒用户，不能购买这个商品。
# 4：可随时退出，退出后，打印已购买商品和余额

# d={1:{'苹果':4},2:{'葡萄':6},3:{'草莓':40},4:{'菠萝':11}}            #定义字典
# sal=int(input('请输入你的工资：'))
# l=[]
# for i in d:
#     for j in d[i]:
#         print('''
#         商品编号：{}
#         商品名称：{}
#         商品价格：{}'''.format(i,j,d[i][j]))
# while True:
#         num=int(input('请输入商品编号：'))
#         if num in d.keys():                                 #判断商品编号否在
#             for m in d[num].keys():                         #获取商品名称
#                 l.append(m)
#                 for n in d[num].values():                   #获取商品价格
#                     print('''
#                     商品名称：{}
#                     商品价格：{}'''.format(m,n))
#                 shu=input("请输入商品数量: ")
#                 if shu.isdigit():
#                     sak=n*int(shu)                           #购买商品应付价钱
#                     if sal>sak:                              #判断工资是否足
#                         sal-=sak                             #剩余工资
#                         print('余额是：{}'.format(sal))
#                     else:
#                         print('很遗憾，你的余额不足，不能购买这个商品！')
#                 else:
#                     print('商品不存在，请重新输入！！！')
#         else:
#             print('请重新输入！！！')
#         zh=input('请问是否继续购买：')                             #判断是否终止购买
#         if zh=='q':
#             print('购买的商品{}，余额为：{}'.format(l,sal))        #打印购买物品和余额
#             break
#         else:
#             continue

# 4、一个足球队在寻找年龄在x岁到y岁的小女孩（包括x岁和y岁）加入。编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。
#循环
# def female_football(k,x=8,y=12):                              #定义函数及参数k,年龄默认8-12岁，k为询问次数
#     c=0                                                         #初始次数为0
#     sum=0                                                       #初始人数为0
#     while True:
#         c+=1
#         age=int(input('请输入你的年龄：'))                    #询问年龄
#         sex=input('请输入你的性别：')                         #询问性别
#         if x<=age<=y:                                         #判断年龄是否符合要求
#             if sex=='f':                                      #判断性别是否符合要求
#                 print('恭喜你可以加入女子足球队！！！')
#                 sum+=1
#             else:
#                 print('很遗憾你的性别不符合要求')
#         else:
#             print('很遗憾你的年龄不符合要求')
#         if c==k:                                              #当达到条件时终止统计
#             break
#     print('满足条件的人数有{}人'.format(sum))
# female_football(5)                                            #传入询问次数