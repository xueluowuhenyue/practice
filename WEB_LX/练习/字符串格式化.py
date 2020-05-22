# 字符串格式化
import json
time='星期一'
mn='星期二'
print('今天是：%s' % '星期一')
print('今天是：{}'.format('星期一'))
print(f'今天是：{time},明天是：{mn}')

# 访问参数的项:
# code=(6, 8)
# str='x:{0[0]};y:{0[1]}'.format(code)
# print(str)
# print(str.split(';'))

# 替代 %x 和 %o 以及转换基于不同进位制的值:
# print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))

# 使用逗号作为千位分隔符:
# print('{:,}'.format(1234567890))

# 表示为百分数:
# points = 19
# total = 22
# print('Correct answers: {:.2%}'.format(points/total))

# 使用特定类型的专属格式化:
# import datetime
# d = datetime.datetime(2010, 7, 4, 12, 15, 58)
# print('{:%Y-%m-%d %H:%M:%S}'.format(d))

# 替代 %+f, %-f 和 % f 以及指定正负号:
# print('{:+f}; {:+f}'.format(3.14, -3.14))

# l=[1,3,5,4,6]
# m=['a','s','d','f','g']
# print(list(set(l)))
# print(dict(zip(m,l)))
# print(list(zip(m,l)))
#
# dict={}
# dict['age']=18
# print(dict)
#
# l=[5,6,7,8,4,1,8,0]
# print(set(l))

l=[51,32,4,9,7,0,4,2,4]
print(set(l))