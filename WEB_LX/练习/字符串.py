# -*- coding:utf-8 -*-
# 字符串 str
'''
a="'hello'"
b="hello word"
print(a)
#统计字符串元素
print(len(a))
#字符串取值从0开始，取值方式：变量名【索引】
print(a[2])
#切片：用法 变量名【m:n:k】从0开始，取左不取右
print(a[1:7:1])
print(b[1:7:2])
'''
# n=0
# for i in b:
#     n+=1
# print(n,end=" ")
'''
#切片倒序
print(b[10::-1])
print(b[::-1])
'''
# 字符串拼接用“+”，不是字符串用“，”str强制转化
# 格式化输出,占位符%s,%d,%f.任何地方都可以放%s
# age=21
# height=170.12
# hobby="钓鱼"
# print('''----绝密档案----
# 年龄是：%d
# 身高是：%0.2f
# 业余爱好是：%s'''%(age,height,hobby))
# 格式化输出二{}
# print('''----绝密档案----
# 年龄是：{0}
# 身高是：{1}
# 业余爱好是：{2}'''.format(age,height,hobby))

# 大小写切换 upper() lower()  swapcase()
b="HelLo Word"
print(b.swapcase())
# 指定字符大、小写
# s=" "
# for i in range(len(b)):
#     if i==8:
#         s+=b[i].upper()
#     else:
#         s+=b[i]
# print(s)
# replace 替换
# s=b.replace(' ','@')
# print(s)
# find 查找元素 没找到返回-1，只考虑正序，不考虑反序
print(b.find('Word')) # 字符串大于一，返回第一个元素的位置（索引）
# capitalize首字母大写
print(b.capitalize())
print(b.count('o'))
print(b.index('r'))
print('@'.join(b)) # H@e@l@L@o@ @W@o@r@d
# 切割
print(b.split(' ')) # 返回列表
print(b.split('o',1))
'''
i=0
say_str = ''
while i<6:
    say = '我说柠檬你说6'
    say_str+=say[-1]
    i +=1
print(say_str)
'''
