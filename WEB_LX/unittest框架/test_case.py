import unittest
from unittest import TestCase
from ddt import ddt,data,unpack
list_data=[[1,2,3],[-1,-3,-4],[2,-5,-3],[6,2,4],[-1,-7,6],[-5,-4,-1]]


@ddt
class TestAdd(unittest.TestCase):
    @data(*list_data)
    def test_math(self,da):
        a = da[0]
        b = da[1]
        c = a+b
        try:
            self.assertEqual(c,da[2])
        except AssertionError as e:
            raise e

    # def test_math(self,a,b,expect):
    #     a = a
    #     b = b
    #     c = a-b
    #     try:
    #         self.assertEqual(c,expect)
    #     except AssertionError as e:
    #         raise e

    # def test_001_two_positive(self):
    #     a = 3
    #     b = 4
    #     c = a+b
    #     print(c)
    #
    # def test_002_two_negative(self):
    #     a = -3
    #     b = -4
    #     c = a+b
    #     print(c)
    #
    # def test_003_negative_positive(self):
    #     a = -3
    #     b = 4
    #     c = a + b
    #     print(c)


# class TestSub(unittest.TestCase):
#     def test_004_two_positive(self):
#         a = 3
#         b = 4
#         c = a-b
#         print(c)
#
#     def test_005_two_negative(self):
#         a = -3
#         b = -4
#         c = a-b
#         print(c)
#
#     def test_006_negative_positive(self):
#         a = -3
#         b = 4
#         c = a - b
#         print(c)


if __name__ == '__main__':
    TestAdd().test_math()
