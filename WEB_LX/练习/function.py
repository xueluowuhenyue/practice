# -*- coding:utf-8 -*-
#函数的定义：实现某个功能 重复使用
#函数的作用：提高代码的复用性
#函数的语法：关键字def
#def 函数名（参数1，参数2，参数三....）
    #函数体：函数要实现的功能
    #return 表达式
#def 顶格表示这是一个函数
#函数名 小写 不同的字母和数字间用下划线隔开 不能用数字开头
#参数个数大于等于0
#函数体是函数的子代码 要有缩进 写要实现的功能
#return后面的表达式大于等于0个
#函数的调用 函数名（对应个数的参数）
# def radio_machine():
#     print('只会说：你好')
#     return
# resuit=radio_machine() #--接收返回值
# print('函数的返回值是：{}'.format(resuit))
# 函数里面return的个数
#等于1 返回指定的数据类型
#大于一时返回的是元组类型
#等于0时返回none
def add():
    result=8+8
    print(result)
    return  result
res=add()+20
print(res)