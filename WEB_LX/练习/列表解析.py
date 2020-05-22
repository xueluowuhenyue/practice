# [表达式 for 元素 in 可迭代对象 if 条件]
# 列表解析式是一种语法糖
# 编译器会优化，不会因为简写而影响效率，反而因优化提高了效率
# 减少程序员工作量，减少出错
# 简化了代码，但可读性增强

# python 列表解析
# 列表解析 List Comprehensions
# 表达式：[expression for iter_val in iterable if cond_expr]
# [expression]：最后执行的结果
# [for iter_val in iterable]：这个可以是一个多层循环
# [if cond_expr]：两个for间是不能有判断语句的，判断语句只能在最后；顺序不定，默认是左到右。

print(sum(range(101)))




# print([(i+1) for i in range(5)])

# print([i for i in range(20) if i%2==0])

# [print(['{}*{}={}'.format(j, i, i*j) for j in range(1, i+1)]) for i in range(1, 10)]

# [print(['%d*%d=%2d' % (j, i, i*j) for j in range(1, i+1)]) for i in range(1, 10)]
# 正序打印乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%d*%d=%2d' % (j, i, i*j), end=' ')
#     print()

# 倒序打印乘法表
# for i in range(9, 0, -1):
#     for j in range(1, i+1):
#         print('%d*%d=%2d' % (j, i, i*j), end='')
#     print()

# 打印质数
# l=[]
# for i in range(1, 101):
#     if i == 1:
#         print('%s不是质数'% i)
#     elif i % 2 == 0:
#         print('%s不是质数'% i)
#     else:
#         for j in range(3, i):
#             if i % j == 0:
#                 print('%s不是质数' % i)
#                 break
#         else:
#             print('%s是质数' % i)
#             l.append(i)
# print(l)

# def jishu(num):
#     if num % 2 !=0:
#         for j in range(3, num):
#             if num % j == 0:
#                 print('%s不是质数' % num)
#                 break
#         else:
#             print('%s是质数' % num)
#     else:
#         print('%s不是质数' % num)
# jishu(19)

# print([i for i in range(5)])


# sum = 0
# for i in range(5):
#     sum += i
# print(sum)