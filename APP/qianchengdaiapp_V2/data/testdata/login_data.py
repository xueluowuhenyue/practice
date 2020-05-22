# -*- coding:utf-8 -*-

mobile_error=[{'Caseid':1, 'module': '登录', 'title': '不填手机号', 'mobile': '', 'text': '无效', 'expect': '无效的手机号'},
              {'Caseid':2, 'module': '登录', 'title': '手机号不以1开始', 'mobile': '2354', 'text': '无效', 'expect': '无效的手机号'},
              {'Caseid':3, 'module': '登录', 'title': '手机号小于11位', 'mobile': '12354', 'text': '无效', 'expect': '无效的手机号'}]


no_register=[{'Caseid':4, 'module': '登录', 'title': '输入不符规则的手机号', 'mobile': '12346466845', 'text': '格式', 'expect': '手机号码格式不正确'},
              {'Caseid': 5, 'module': '登录', 'title': '未注册账号登录', 'mobile': '13541781424', 'text': '验证码', 'expect': '请输入验证码'}]

pwd_error=[{'Caseid':6, 'module': '登录', 'title': '不输入密码', 'mobile': '18684720553', 'pwd': '25464', 'text': '', 'expect': '手机号或密码错误'},
           {'Caseid':7, 'module': '登录', 'title': '密码错误', 'mobile': '18684720553', 'pwd': '25464', 'text': '错误', 'expect': '手机号或密码错误'}]

login_success=[{'Caseid':8, 'module': '登录', 'title': '正常登录', 'mobile': '18684720553','pwd': 'python', 'expect': '小蜜蜂96027921'}]  #九重天小蜜蜂9602792