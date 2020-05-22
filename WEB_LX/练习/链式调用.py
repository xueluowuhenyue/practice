# -*- coding:utf-8 -*-
list=[]

def kh():
    print('666')
def kn():
    print('555')

def km():
    print('777')

def kk():
    print('888')

list.append(kh)
list.append(kn)
list.append(km)
list.append(kh)

for i in list:
    i()