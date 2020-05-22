import requests
# 接口地址： http://test.lemonban.com/futureloan/mvc/api/member/login
# 接口参数： {'mobilephone':'#mobilephone#','pwd':'#password#'}  13541781424
# 期望结果： {'status':1,'code':'10001','data':None,'msg':'登录成功'}


class Login:

    def Mock_Login(self, mobile_phone, pwd):
        url='http://test.lemonban.com/futureloan/mvc/api/member/login'
        data={'mobilephone': mobile_phone, 'pwd': pwd}
        resp = requests.post(url, data=data)
        return resp.json()['code']

    def login(self, mobile_phone, pwd):
        res = self.Mock_Login(mobile_phone, pwd)
        if res == 10001:
            print('登录成功')
            return {'status':1,'code':'10001','data':None,'msg':'登录成功'}
        elif res == 20103:
            print('密码不能为空')
            return {'status':0,'code':'20103','data':None,'msg':'密码不能为空'}
        elif res == 20111:
            print('用户名或密码错误')
            return {'status':0,'code':'20111','data':None,'msg':'用户名或密码错误'}
        else:
            return '输入错误'









