# [表达式 for 元素 in 可迭代对象 if 条件]
# 列表解析式是一种语法糖
# 编译器会优化，不会因为简写而影响效率，反而因优化提高了效率
# 减少程序员工作量，减少出错
# 简化了代码，但可读性增强

# print([(i+1) for i in range(5)])

print([i for i in range(20) if i%2==0])

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

[print(['%d*%d=%2d' %(i, j, j*i) for j in range(1, i+1)])for i in range(1, 10)]