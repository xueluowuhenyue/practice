# 函数作用域
# global 声明全局变量 nonlocal声明非本地变量
# local 局部作用域，本地哦作用域
# enclosing 嵌套作用域
# global 全局作用域
# built-in 内建作用域
# age = 20
# def output():
#     age = 18
#
#     def outer():
#         nonlocal age
#         print(f"局部变量的值是{age}")
#
#     print(f"嵌套变量的值是{age}")
#     outer()
# print(f"全局变量的值是{age}")
# output()

# 1、map 函数
# l=[1,2,3,4,5]
# def de(num):
#     return num**2
# print(list(map(de,l)))

# 2、filter 函数
# l=[1,2,3,4,5]
# def de(num):
#     if num %2 == 0:
#         return num**2
# print(list(filter(de,l)))

# 3、lembda 匿名函数
# 没有名字的函数就是匿名函数，并且因为匿名函数没有名字，所以不必担心函数名冲突；
# 在Python中，借助lambda表达式构建匿名函数，关键字lambda表示匿名函数，冒号前面的变量名表示函数参数；
# 匿名函数可以实现自调用（也就是自己调用自己）；
# l=[1, 2, 3, 4, 5]
# print(list(map(lambda i: i**2, l)))
# a = ['a', 'b', 'c'],b = ['d', 'e', 'f']利用map()函数和lambda函数生成列表['ad','be','cf']
# zip函数返回一个元组对象
# 6789
# print(list(zip(a,b)))
# print([a[i] + b[i] for i in range(len(a))])
# print(list(map(lambda i: i[0]+i[1], zip(a, b))))

# 偏导数
# import functools
# def add(a,b):
#     return a+b
# res = functools.partial(add,3)
# print(res(2))

# 5、递归函数
# 递归函数的特性
# 递归一定需要有结束条件；
# 每次进入更深一层递归时，问题规模比上一次递归都应有所减少；
# 通常前一次递归的输出就作为后一次递归的输入；
# 递归效率不高，递归层次过多会导致栈溢出；
# 计算阶乘
# a= int(input("请输入一个数字："))
# b = 1
# sum = 1
# while b <= a:
#     sum *= b
#     b += 1
# print(sum)

# 二 利用递归函数计算阶乘
# def add(num):
#     if num==1:
#         return 1
#     return num*add(num-1)
# while True:
#     num = int(input("请输入一个数字："))
#     print(add(num))
#     if num >= 100:
#         break

# 计算斐波那契数列1、1、2、3、5、8、13、21、34
# def add(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     return add(n-1)+add(n-2)


# 统计输入数据的结果
# l = []
# while True:
#     n = int(input("请输入一个数字："))
#     l.append(add(n))
#     if n >=10:
#         break
#     print(l)

# 统计当前数据之前的结果
# n = int(input("请输入一个数字："))
# print([add(i) for i in range(1,n+1)])

# import sqlite3
# conn=sqlite3.connect('mrsoft.db')
# cursor=conn.cursor()
# cursor.execute('create table user(id int(10) primary key, name varchar(20))')
# cursor.close()
# conn.close()

# 保护属性
# class m:
#     _kn_g='45'
#     def p(self):
#         print(self._kn_g)
#         print(m._kn_g)
# bn=m()
# bn.p()

# 私有属性
# class m:
#     __kn_g='45'      # 私有属性
#     def p(self):
#         print('类调用私有属性p：%s' %(m.__kn_g),666)
# bn=m()
# # 加入类名调用
# print(bn._m__kn_g)
# bn.p()

# 计算1-10的和
# 1.
# print(sum(range(1, 11)))
# 2.
# sum = 0
# for i in range(1,11):
#     sum += i
# print(sum)
# 3.
# res = 0
# n = int(input("请输入一个数："))
# i = 1
# while i <= n:
#     for i in range(1, n+1):
#         res = res + i
#         i += 1
#     print(res)