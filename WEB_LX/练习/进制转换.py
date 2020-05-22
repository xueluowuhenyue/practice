# -*- coding:utf-8 -*-

# a=16
# # 十进制转二进制
# j=bin(a)
# print(j)
# # 十进制转八进制
# j=oct(a)
# print(j)
# # 十进制转十六进制
# j=hex(a)
# print(j)
#
# b='100000'
# # 二进制转十进制
# j=int(b, 2)
# print(j)
# # 二进制转八进制
# j=int(b, 8)
# print(j)
#
# # 二进制转十六进制
# j=int(b, 16)
# print(j)

# 集合 set
a=[3,2]
m=[5,6,8,9,4,7,9]
n=set(m)
n.add(0)
n.remove(8)
n.pop()
# 集合合并
# print(set(a) | set(m))
# print(set(a).union(set(m)))
k=n.union(set(a))
print(k)