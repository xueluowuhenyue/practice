# -*- coding:utf-8 -*-
# 字符串格式化
time='星期一'
print('今天是：%s' % '星期一')
print('今天是：{}'.format('星期一'))
print(f'今天是：{time}')
# l='hello word'
# 第一种
# m=' '.join(l.split(' ')[::-1])
# print(m)
# n=['word','hello']
# print(' '.join(n))
# 第二种
# s=''
# m=l.split(' ')[::-1]
# for i in m:
#     s+=i
#     s+=' '
#     s.strip(' ')
# print(s)
# import chardet
# a='abbacc'
# b='fkkfll'
# m=enumerate(a)
# n=enumerate(b)
# print(m)
# print(n)

# str1='abbacc'
# str2='bccbdd'
#
#
# def encoder(str1):
#     code={}
#     for i in str1:
#         code[i] = None
#     print(code)
#     for key,value in enumerate(code):
#         str1 = str1.replace(value, str(key))
#         print(str1)
#     return str1
#
#
# def is_name(str1, str2):
#     str1=encoder(str1)
#     print(str1)
#     str2 = encoder(str2)
#     print(str2)
#     if str1==str2:
#         return True
#     else:
#         return False
# print(is_name(str1, str2))

# 字符串格式化
# name='hehe'
# age=18
# print(f'姓名是：{name},年龄是：{age}')

# l=[5,1,32,4,0,6,7]
# s=[8]
# l.reverse()     # 倒序
# print(l[-1::-1])
# # print(l[::-1])
# l.pop()        # 删除 按索引删除
# l.remove(6)      # 按值删除
# l.clear()      # 清空
# l.extend(s)      # 列表合并
# print(l+s)        # 列表合并
# l.count(9)           # 计算次数
# l.insert(2,2)      # 添加元素

# 编程: 如果一个字典里键名为"张三"的值为None，就给它赋一个值
# d='name'
# if isinstance(d,dict):
#     if d['name'] == None:
#         d['name']='zhang'
#         print(d)
#     else:
#         print(d)

# 将字符串a="1234567"倒序输出，请用多种方法实现
a="1234567"
# # print(a[::-1])
b=list(a)
b.reverse()
# print(''.join(b))
# s=''
# for i in b:
#     s+=i
# print(s)
# 2. 将列表a = ["h","e","l","l","o"]拼接成字符串，请用多种方法实现
# a = ["h","e","l","l","o"]
# # b=''.join(a)
# # print(b)