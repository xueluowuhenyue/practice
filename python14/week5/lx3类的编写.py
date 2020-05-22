# class SuperMan():
#     #类属性
#     name='linfu'
#     age=20
#     sex='f'
#     #类的方法
#     def protect_people(self):
#         print('我是超人')
#     def fly_to_sky(self):
#         print('我会飞')
#1、调用
#使用类调用        
# SuperMan().fly_to_sky()

#使用类调用属性
# print(SuperMan().age)

#创建实例调用
# p=SuperMan()
# p.protect_people()

# #创建实例调用属性
# print(p.sex)

#2、类函数调用类属性
# class SuperMan():
#     #类属性
#     name='linfu'
#     age=20
#     sex='f'
#     #类的方法
#     def protect_people(self):
#         print('我是超人，我的名字是:%s'%self.name)
# p=SuperMan()
# p.protect_people()    

#3、类函数调带有位置参数
# class SuperMan():
#     #类属性
#     name='linfu'
#     age=20
#     sex='f'
#     #类的方法
#     def protect_people(self,name):
#         print('我是超人，我的名字是:%s'%name)
# p=SuperMan()
# p.protect_people('华华')  

#4、类函数调带有默认参数
# class SuperMan():
#     #类属性
#     name='linfu'
#     age=20
#     sex='f'
#     #类的方法
#     def protect_people(self,name='毛毛'):
#         print('我是超人，我的名字是:%s'%name)
# p=SuperMan()
# p.protect_people()  

#5、类函数内调用不带参数的内函数 函数前要加关键字self
# class SuperMan():
#     #类属性
#     name='linfu'
#     age=20
#     sex='f'
#     #类的方法
#     def protect_people(self,name='毛毛'):
#         print('我是超人，我的名字是：%s'%name)
#         self.fly_to_sky()
#     def fly_to_sky(self):
#         print('我会飞')
# p=SuperMan()
# p.protect_people()  

#5、类函数内调用带参数的内函数 函数前要加关键字self
# class SuperMan():
#     #类属性
#     name='linfu'
#     age=20
#     sex='f'
#     #类的方法
#     def protect_people(self,name='毛毛'):
#         print('我是超人，我的名字是：%s'%name)
#     def fly_to_sky(self):
#         self.protect_people('小简')
#         print('我会飞')
# p=SuperMan()
# p.fly_to_sky()  

#6、类函数内调用带动态参数
# class SuperMan():
#     #类属性
#     name='linfu'
#     age=20
#     sex='f'
#     #类的方法
#     def protect_people(self,*args):
#         for name in args:
#             print('我是超人，我的名字是：%s'%name)
# p=SuperMan()
# p.protect_people('华华','小简','丹丹','星星')
#7、类函数内调用带关键字参数         
# class SuperMan():
#     #类属性
#     name='linfu'
#     age=20
#     sex='f'
#     #类的方法
#     def protect_people(self,**kwargs):
#         print('我是超人，我的信息是：%s'%kwargs)
# p=SuperMan()
# p.protect_people(name='华华',age=25,height=180,hobby='钓鱼')  

#8、类的初始化函数__init__
# class SuperMan():
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def protect_people(self):
#         print('我是超人')
#     def fly_to_sky(self):
#         print('我会飞')
# p=SuperMan('华华',25,'f')     #创建对象
# p.protect_people()           #调用类的方法
# print(p.age)                 #调用类属性

#8、类函数调用初始化值   必须加关键字self
# class SuperMan():
#     def __init__(self,age,sex,name='星星'):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def protect_people(self):
#         print('我是超人，我的名字是：%s'%self.name)
# p=SuperMan(25,'f','华华')     #创建对象
# p.protect_people()           #调用类的方法
# print(p.age)                 #调用类属性        