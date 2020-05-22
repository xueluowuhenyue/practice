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
a=[1,7,4,89,34,2]
for i in range(len(a)-1):                   #循环次数
    for j in range(len(a)-1):
        if a[j]>a[j+1]:                     #位置交换
            k=a[j]
            a[j]=a[j+1]
            a[j+1]=k
print(a)
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
