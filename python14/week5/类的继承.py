#1.类的继承简单用法
# class SoftwareTestEngineer:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def basic_skill(self):
#         print(self.name+'今年'+str(self.age)+'岁')
#     def salary(self,salary):
#         print('薪资大概是%s'%salary)
# # SoftwareTestEngineer('华华',24).basic_skill()    
# # SoftwareTestEngineer('华华',24).salary('6000-8000')
# 
# class juniorSoftwareTestEngineer(SoftwareTestEngineer):
#     pass
# juniorSoftwareTestEngineer('华华',24).basic_skill()
# juniorSoftwareTestEngineer('华华',24).salary('6000-8000')


#2.类的继承重写和拓展
#重写
# class juniorSoftwareTestEngineer(SoftwareTestEngineer):
#     def basic_skill(self):
#         print(self.name+'今年'+str(self.age)+'岁'+'可以完成点点点测试')
# juniorSoftwareTestEngineer('华华',24).basic_skill()
# juniorSoftwareTestEngineer('华华',24).salary('6000-8000')        

#拓展
# class juniorSoftwareTestEngineer(SoftwareTestEngineer):
#     def basic_skill(self):
#         print(self.name+'今年'+str(self.age)+'岁'+'可以完成点点点测试') 
#     def auto_test(self,code):
#         print(self.name+'能够做%s自动化测试'%code)       
# juniorSoftwareTestEngineer('星星',24).auto_test('python')
# juniorSoftwareTestEngineer('毛毛',24).salary('6000-8000') 

#3.类的多继承
# class A:
#     def add(self,a,b):
#         print('A类中的加法',a+b)
# class B:
#     def sub(self,a,b):
#         print('B类中的减法',a-b)      
# class c(A,B):
#     pass
# c().add(5,2)
# c().sub(8,4)

# 4.类的超继承
# class SeniorSoftwareTestEngineer(juniorSoftwareTestEngineer): 
#     def auto_test(self,code):
#         super(SeniorSoftwareTestEngineer,self).auto_test(code)
#         print('我还可以做接口自动化、web自动化、app自动化') 
# SeniorSoftwareTestEngineer('星星',24).auto_test('python')
