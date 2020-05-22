# -*- coding:utf-8 -*-
# 初始化函数--魔方函数  魔法函数
class BoyFriend:
    def __init__(self,age,height,name):    #初始化函数
        self.age=age
        self.height=height
        self.name=name

    #函数 传参和普通函数一样
    def sport(self,*args):               #第一个参数是self 类里面函数的标致
        print(self.name+'喜欢运动:{}'.format(args))

    @classmethod                    #类函数
    def cook(cls):
        print('会下厨做饭')

    @staticmethod                  #静态函数
    def coding():                 #静态函数要写在类里面，但是跟其他属性和函数无调用关系
        print('会写代码')

#创建对象/实例
p=BoyFriend(22,180,'梅西')
# p.cook()                       #通对象调用类函数
# BoyFriend.cook()               #通过类调用类函数
# p.coding()                     #通对象调用静态函数
# BoyFriend.coding()             #通过类调用静态函数
# print(p.name)
p.sport('打乒乓','足球')
