# 1：人和机器猜拳游戏写成一个类，有如下几个函数：
# 1）函数1：选择角色1 曹操 2张飞 3 刘备
# 2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
# 3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
# 4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
# 5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
# import random
# class peopleComputerGreatWar:
#     '''人机游戏类'''
#     dict_2={1:'剪刀',2:'石头',3:'布'}
#     c=0                                                     #电脑计数
#     p=0                                                     #人胜计数
#     k=0                                                     #平局
#     def role(self):
#         '''角色选择：1代表曹操，2代表张飞，3代表刘备'''
#         while True:
#             dict_1={1:'曹操',2:'张飞',3:'刘备'}
#             num=int(input('请输入角色编号：'))
#             if num in range(1,4):
#                 print('你选的角色是：{}'.format(dict_1[num]))
#                 return dict_1[num]
#             else:
#                 print('你输入的角色编号不存在，请重新输入')
#     def roleFingerGuessingGame(self):
#         '''角色出拳  1代表剪刀,2:代表石头,3代表布'''
#         while True:
#             num_1=int(input('请输入出拳编号： '))
#             if num_1 in range(1,4):
#                 print('角色出的拳是：{}'.format(self.dict_2[num_1]))
#                 return num_1
#             else:
#                 print('出拳的编号不存在，请重新输入')
#     def computerPunches(self):
#         '''电脑出拳   1代表剪刀,2:代表石头,3代表布'''
#         num_2=random.randint(1,3)
#         if num_2 in range(1,4):
#             print('电脑出的拳是：{}'.format(self.dict_2[num_2]))
#             return num_2
#     def roleComputer(self):
#         '''人机对战'''
#         name=self.role()
#         while True:
#             m=self.roleFingerGuessingGame()               #获取角色出拳编号
#             n=self.computerPunches()                      #获取电脑出拳编号
#             if n-m in [1,-2]:
#                 print('电脑获胜')
#                 self.c+=1
#             elif n-m==0:
#                 print('平局')
#                 self.k+=1
#             else:
#                 print('%s获胜'%name)
#                 self.p+=1
#             choice=input('请问是否继续游戏： ''y表示继续,n表示退出')
#             if choice=='n':                                   #输入n终止游戏，其他字符继续游戏
#                 print('电脑获胜{}，{}获胜{}，平局{}'.format(self.c,name,self.p,self.k))
#                 break

# 2：编写一个类：你们自行去设计，要求写一个类， 初始化函数 对象函数 包含 根据你不同的选择完成get请求
# OR post请求 ，其中url 需要做参数化，并且最后要拿到响应结果
# import requests
# class httpRequests:
#     '''这是一个发送http请求的类'''
#     def __init__(self,url,method='get'):
#         '''url参数化'''
#         self.url=url
#         self.method=method
#     def request(self):
#         if self.method.lower()=='get':
#             res=requests.get(self.url)                            #发送请求，接收响应数据
#             print('get请求的状态码是：%s'%(res.status_code))      #打印状态码
#         else:
#             res=requests.post(self.url)
#             print('post请求的状态码是：%s'%(res.text))
# if __name__ == '__main__':
#第一题
    # p=peopleComputerGreatWar()
    # p.roleComputer()
#
#     #第二题
#     p=httpRequests('https://www.baidu.com')
#     p.request()                                    #发送get请求
#     httpRequests('https://www.ketangpai.com','dd').request()   #发送post请求