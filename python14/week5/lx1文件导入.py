#import 用法
# import lx.sub_1.a
# import lx.sub_2.b
# lx.sub_1.a.add(5,2)
# lx.sub_2.b.sub(5,2)

#from.....import 用法
# from lx.sub_1 import a
# from lx.sub_2.b import sub
# a.add(2,5)
# sub(6,1)

# import  as用法
import lx.sub_1.a as m
import lx.sub_2.b as n
m.add(5,2)
n.sub(5,2)