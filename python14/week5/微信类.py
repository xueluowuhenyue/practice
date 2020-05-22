class WeChat:
    '''这是一个微信类'''
    #属性
    year='2011'
    company='腾讯'
    pm='张晓龙'
    #函数
    def add_friends(self):
        '''添加好友'''
        print('具有添加好友的功能')

    def send_msg(self):
        '''发送信息'''
        print('具有发送信息的功能')
#抽象的东西 具有继承的特性 复用性高
#调用：实例化  类名（）
t=WeChat()    #对象实例
print(t.pm)   #调用属性