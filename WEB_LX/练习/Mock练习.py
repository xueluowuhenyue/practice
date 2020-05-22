# -*- coding:utf-8 -*-
from unittest import mock
import requests
import json


class Login:
    def loginapi(self, username, password):
        '''
        :param username: 登录名
        :param password: 密码
        :param mac:     物理地址
        :return: res  登录结果
        '''
        url='http://www.baidu.com'  # 第三方接口地址
        data={'username':username,'password':password}
        res = requests.post(url, data=data)
        return res.json()["resultCode"]

    def login(self, username, password):
        try:
            result=self.loginapi(username, password)
        except TimeoutError:
            result = self.loginapi(username, password)

        if result == 200:
            res= {"success": "true", "msg": "登录成功", "resultCode": "200",
                      "obj":{"userId": "22", "userName":"Freshing Air","userType": "3"}}
            return res
        elif result == 403:
            if username == '':
                res= '{"resultCode":403,"obj":null,"success":false,"msg":"用户名不能为空","token":null}'
                return json.loads(res)
            elif username == 'freshingair' and password == '':
                res=  '{"resultCode":403,"obj":null,"success":false,"msg":"密码不能为空","token":null}'
                return json.loads(res)
            elif username != 'freshingair':
                res=  '{"resultCode":403,"obj":null,"success":false,"msg":"登录名错误","token":null}'
                return json.loads(res)
            else:
                res= '{"resultCode": 403, "obj": null, "success": false, ' \
                      '"msg": "密码错误！请重新输入正确的密码！", "token": null}'
                return json.loads(res)
        else:
            return '服务器故障'


if __name__ == '__main__':
    login=Login()
    # login.loginapi=mock.Mock(return_value=403)
    # # res=login.login('freshingair','123456')
    # res = login.login('freshingair', '')
    # res_2 = login.login('', '123456')
    # res_3 = login.login('freshingair', '1562556')
    # print(res)
    # print(res_2)
    # print(res_3)
    login.loginapi = mock.Mock(side_effect=[TimeoutError, 403])
    res_3 = login.login('', '12347')
    print(res_3)