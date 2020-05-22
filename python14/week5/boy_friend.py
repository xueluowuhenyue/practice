# -*- coding:utf-8 -*-
class BoyFriend:
    sex='男'
    age=28
    height=180
    weight=150
    name='彭于晏'

    #函数  传参和普通函数一样
    def sport(self,sport_type):               #第一个参数是self 类里面函数的标致
        print(self.name+'喜欢运动:{}'.format(sport_type))
        # print('类的函数里打印self：',self)
        # self.coding()                #函数调用

    @classmethod                    #类函数
    def cook(cls):
        print('会下厨做饭')
        cls().coding()              #类函数中调用函数

    @staticmethod                  #静态函数
    def coding():                 #静态函数要写在类里面，但是跟其他属性和函数无调用关系
        print('会写代码')

#创建对象/实例
# p=BoyFriend()
# p.cook()                       #通对象调用类函数
# BoyFriend.cook()               #通过类调用类函数
# p.coding()                     #通对象调用静态函数
# BoyFriend.coding()             #通过类调用静态函数
# print(p.name)
# p.sport('打乒乓')
# print('类的函数里打印对象p:',p)

#类里面的函数有三种 对象方法 类方法 静态方法
#对象方法        只能被对象调用
# 类方法         类函数可以被对象和类调用    关键字@classmethod
# 静态方法       静态函数可以被对象和类调    关键字@staticmethod