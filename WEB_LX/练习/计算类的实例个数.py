# -*- coding:utf-8 -*-
# python 计算创建类的实例的个数


class X(object):
    count=0

    def __new__(cls):
        cls.count =cls.count+1
        return super(X,cls).__new__(cls)

    def Count(self):
        print(self.count)

    def __init__(self):
        pass


if __name__=="__main__":
    a=X()
    b=X()
    c=X()
    d=X()
    a.Count()

