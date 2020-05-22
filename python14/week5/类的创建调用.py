#1：编写一个数学类，要求初始化函数带a,b,c,d4个参数，然后有加减乘数四个函数
# class math:
#     ''''这是一个数学类'''
#     def __init__(self,a,b,c,d):
#         '''参数化'''
#         self.a=a
#         self.b=b
#         self.c=c
#         self.d=d
#     def addFunction(self):          #对象函数
#         '''这是一个加法函数'''
#         print(self.a+self.b)
#     def subFunction(self):
#         '''这是一个减法函数'''
#         print(self.b-self.c)
#     def multiplicationFunction(self):
#         '''这是一个乘法函数'''
#         print(self.d*self.c)
#     @classmethod                    #类函数
#     def divisionFunction(cls):
#         '''这是一个除法函数'''
#         print(cls(5,6,8,4).a/cls(5,9,2,3).d)
#     @staticmethod                   #静态函数
#     def functionInfo():
#         print('这是函数信息')
# m=math(5,6,7,9)                     #创建实例
# m.functionInfo()                    #通过对象调用静态函数
# math.functionInfo()                 #通过类调用静态函数
# math.divisionFunction()             #通过类调用类函数
# m.divisionFunction()                #通过对象调用类函数
# m.addFunction()                     #通过对象调用对象函数

#2：依靠自己的想象力，编写一个软件测试工程师类，要求包含初始化函数 类函数 对象函数  静态函数
# class SoftwareTestEngineer:
#     '''这是一个测试工程师类'''
#     def __init__(self,name,age,height):
#         '''信息参数化'''
#         self.name=name
#         self.age=age
#         self.height=height
#           
#     def personageInfo(self,*args): 
#         '''个人信息'''                                #对象函数     
#         print('我的名字是：{},今年{}岁,身高{},爱好有:{}'.format(self.name,self.age,self.height,args))    
#        
#     @classmethod                                      #类函数
#     def salaryInfo(cls,salary):
#         '''工资信息'''
#         print('现在工资大约是{}'.format(salary))
#                  
#     @staticmethod                                     #静态函数
#     def skill():
#         print('个人技能有：会敲代码、会做饭')
#          
# p=SoftwareTestEngineer('小明',25,175)                  #创建对象
# p.personageInfo('爬山','钓鱼','打乒乓','跑步')             #通过对象调用对象函数
# p.salaryInfo('5500-8000')                             #通过对象调用类函数
# SoftwareTestEngineer.salaryInfo('8000-10000')         #通过类调用类函数
# p.skill()                                             #通过对象调用静态函数
# SoftwareTestEngineer.skill()                          #通过类调用静态函数