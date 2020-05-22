import unittest
from unittest import mock
from lx_Python.mock模块 import class_mock


class MockTest(unittest.TestCase):

    def test_01_success_login(self):
        login=class_mock.Login()
        login.Mock_Login = mock.Mock(return_value=10001)
        expectcd = {'status': 1, 'code': '10001', 'data': None, 'msg': '登录成功'}
        res = login.login(13541781424, 123456)
        try:
            self.assertEqual(res, expectcd)
        except AssertionError as e:
            print('断言错误')
            raise e

    def test_02_empty_phone(self):
        login = class_mock.Login()
        login.Mock_Login = mock.Mock(return_value=20103)
        expectcd = {'status':0,'code':'20103','data':None,'msg':'密码不能为空'}
        res = login.login(13541781424, '')
        try:
            self.assertEqual(res, expectcd)
        except AssertionError as e:
            print('断言错误')
            raise e

    def test_03_empty_pwd(self):
        login = class_mock.Login()
        login.Mock_Login = mock.Mock(return_value=20111)
        expectcd = {'status':0,'code':'20111','data':None,'msg':'用户名或密码错误'}
        res = login.login(13541781424, 12326797)
        try:
            self.assertEqual(res, expectcd)
        except AssertionError as e:
            print('断言错误')
            raise e


if __name__ == '__main__':
    unittest.main()