# -*- coding:utf-8 -*-
#1.根据你输入的数据，来进行判断学生的成绩。输入数据函数：input()
# score=int(input('请输入你的分数：'))
# if 0<=score<=100:
#     if score<60:
#         print('不及格')
#     elif 60<=score<75:
#         print('及格')
#     elif 75<=score<90:
#         print('良好')
#     else:
#         print('优秀')
# else:
#     print('无效分数请重新输入')

# 2、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
# 如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格
# price=float(input('请输入商品的价格：'))
# if 50<=price<=100:
#     print('你需要支付的价钱是：{}'.format(0.9*price))
# elif 100<price:
#     print('你需要支付的价钱是：{}'.format(0.8*price))
# else:
#     print('你需要支付的价钱是：{}'.format(price))

#3、输入一个数，判断一个数n能同时被3和5整除
# num=input('输入一个数：')
# if num.isdigit()==True:
#     if int(num)%3==0:
#         if int(num)%5==0:
#             print('恭喜你输入正确')
#         else:
#             print('很遗憾，该数字不能被5整除')
#     else:
#          print('很遗憾，该数字不能被3整除')
# else:
#     print('请重新输入')

#4、输入一个年份，输出是否为闰年，闰年条件：能被4整除但不能被100整除，或者能被400整除的年份都是闰年
#year=int(input('请输入一个整数：'))
# if year%400==0:
#     print('闰年')
# elif year%4 == 0:
#     if year%100!=0:
#         print('闰年')
#     else:
#         print('平年')
# else:
#     print('平年')
#5、一个 5 位数，判断它是不是回文数。即 12321 是回文数，个位与万位相同，十位与千位相同。 根据判断打印出相关信息。
# num=int(input('输入一个五位数：'))
# if len(str(num))==5:
#     if str(num)[0]==str(num)[4]:
#         if str(num)[1]==str(num)[3]:
#             print('这个数是回文数')
#         else:
#             print('这个数不是回文数')
#     else:
#         print('这个数不是回文数')
# else:
#     print('请重新输入')
#6、生成随机整数，从1-9取出来。然后输入一个数字，来猜，如果大于，则打印bigger。小了，则打印less。如果相等，则打印equal
# import random
# num=random.randint(1,9)
# print(num)
# m=input('输入一个数：')
# if m.isdigit()==True:
#     if int(m)>num:
#         print('bigger')
#     elif int(m)<num:
#         print('less')
#     else:
#         print('equal')
# else:
#     print('请重新输入：')
# 7、写一个餐厅菜单显示程序：（大概的设计模式如下） 请自己设计一个数据存储这些菜单，然后根据你从客户端输入的数据去进行菜名的读取
# d={'平价菜':{'手撕包菜':'10元','大白菜':'10元','土豆丝':'10元'},'凉菜':{'凉拌黄瓜':'8元','凉拌皮蛋':'9元'},
#        '小锅现炒':{'水煮鸡':'26元','红烧鱼块':'18元'}}
# Vegetables=input('请选择分类：')
# if Vegetables in d.keys():
#     name=input('请选择菜名：')
#     if name in d[Vegetables].keys():
#         print('你选的菜是：{}，价格是{}'.format(name,d[Vegetables][name]))
#     else:
#         print('很遗憾，你点的菜本店没有，请重新选择')
# else:
#     print('很遗憾，你点的菜类本店没有，请重新选择')
#二
# name=input('请输入名字：')
# l=[]
# k=[]
# for i in d.keys():
#     for j in d[i]:
#         l.append(j)
# for m in d.values():
#     for n in m.values():
#         k.append(n)
# h=dict(zip(l,k))
# if name in h.keys():
#     print('你选择的菜是:{},价格是：{}'.format(name,h[name]))
# else:
#     print('很遗憾，你点的菜类本店没有，请重新选择')
