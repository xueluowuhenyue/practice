# -*- coding:utf-8 -*-
# while循环;可以无限次数循环--死循环 可以加条件控制循环
# where循环表达式:
    # 循环体
# 条件表达式：跟if一样
# 1.一般逻辑运算 比较运算 成员运算
# 2.非0或非空表示True 0或空的数据 表示False
# 3.可以用布尔值来代替表达式

# 运行模式：判断while后面的条件 满足 执行循环 不满足 不执行
# 执行完毕后再次判断条件满足 执行循环 不满足 不执行 如此反复
# 怎么达到不是绝对的True 和False
# 1.基本解决办法：break 中断循环 用的不好只执行一次
# 2.进阶使用break+条件，规定循环多少次
# 3.高级使用：必要的时候脱离break
# a=0
# while True:
#     a+=1
#     print('a的值：',a)
#     if a==5:
#         break
#     print("死循环".format(a))
# a=0
# while a<10:
#     a+=1
#     print('a的值：',a)
#     if a==5:
#         break
#     print("死循环".format(a))
# 一个足球队寻找年龄在10到12岁的女孩加入，然后显示一条消息指出这个人是否可以加入球队询问10次
# 满足输出
# if 判断
# for循环
# input
# count=0#记录满足条件单人数
# for i in range(1,11):
#     age=int(input('请问你今年多少岁？'))
#     if 10<=age<=12:
#         sex=input('请填一下你的性别')
#         if sex=='f':
#             print('恭喜你，可以加入我们球队')
#             count+=1
#         else sex != 'f':
#             print('很遗憾你的性别不符合要求')
#     else:
#         print('不好意思，你的年龄不符合要求')
# print('满足条件的人数有:{0}'.format(count))

# 2.一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，
# 输出满足条件的总人数。

# a=input('请问你今年多少岁： ')
# while c<10:
#     if   10<=int(a)<=12:
#         b=input('请问你的性别是：')
#         if b=='f':
#             print('恭喜你可以加入球队')
#         else:
#             print('不合格')
#     else:
#
#         print('不合格')
#     c+=1
# num=0
# for i in range(1,11):
#     a=input('请问你今年多少岁： ')
#     if   10<=int(a)<=12:
#         b=input('请问你的性别是：')
#         if b=='f':
#             print('恭喜你可以加入球队')
#             num+=1
#         else:
#             print('不合格')
#     else:
#         print('不合格')
# print('符合条件的人数是{}'.format(num))
list1 = [[2, 3, 8, 4, 9, 5, 6],[5, 6, 10, 17, 11, 2]]
for i in list1:
    for j in i:
        print(j)