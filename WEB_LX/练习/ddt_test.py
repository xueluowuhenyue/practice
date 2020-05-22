# -*- coding:utf-8 -*-
import unittest
from ddt import ddt,data,unpack

# @ddt
# class ddt_test(unittest.TestCase):
#     t=(1,2,5),(4,2,6),(5,6,12)
#     d=[{'a':2,'b':3,'expected':6},{'a':4,'b':0,'expected':6}]
#     @data(*t)
#     @unpack
#     def test_001(self,a,b,expect):
#         c=a+b
#         self.assertEqual(c,expect)
#       def test_002(self,d):
#           c=d['a']+d['b']
#           self.assertEqual(c,d['expected'])


# sum = 0
# def add_test(*args):
#     for i in args:
#         global sum
#         sum+=i
#     return sum
#
# res=add_test(1,3,6)
# print(res)
