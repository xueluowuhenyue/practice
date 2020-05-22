# -*- coding:utf-8 -*-

error_bid=[{'Caseid':1, 'module': '投标', 'title': '不输入金额 ', 'amount': '', 'text': '请输入', 'expect': '请输入投资金额'},
           {'Caseid':2, 'module': '投标', 'title': '投资金额为0 ', 'amount': '0', 'text': '最小投资', 'expect': "最小投资金额为:100.0"},
           {'Caseid':3, 'module': '投标', 'title': '投资金额不是100的整倍数 ', 'amount': '321', 'text': '必须', 'expect': '投资金额必须为100的整数倍'},
           {'Caseid':4, 'module': '投标', 'title': '投资金额大于余额 ', 'amount': '50000', 'text': '余额', 'expect': '余额不够'}]

success_bid=[{'Caseid':5, 'module': '投标', 'title': '正常投资 ', 'amount': '100', 'expect': '投资成功'}]