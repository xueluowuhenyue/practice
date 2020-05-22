# 列表  tuple 以中括号【】括起的数据，看类型 type 空列表【】
# 1、元素间用，隔开，看长度用len
# 3、取值方法，与字符串/元组一致，根据索引，可切片
# 4、列表中可以包含各种累心的数据：整数、浮点数、布尔值....
# 取单个值 列表名【，索引值】，从0开始
# 嵌套取值，层层取
# 切片，同字符串、元组一样
# 列表有序，可修改（增删改）
# m=['a',2,['python'],'haha',(1,2,3),1.25]
# print(len(m))
# print(m[-2])
# print(m[4][1])
# print(m[0::2])
# print(m[-2][0:3:2])
# print(m.count(2))
# print(m.clear())
# 1.append每次只能增加一个元素
# m.append("哈哈")
# print(m)
# 2.指定索引位置加元素 列表.insert(i,volue),每次加一个元素
# m.insert(2,5)
# print(m)
# 3.添加列表  列表名.extend(第二个列表名)合并列表
# n=[6,8,9]
# m.extend(n)
# print(m)
# print(m+n)
# 删除元素
# 1.删除最后一个元素 列表名.pop()
# print(m.pop())
# 2.删除指定位置元素
# m.pop(2)
# print(m)
# s=[1,2,3,3,4,8]
# b=str(s)
# b=tuple(s)
# print(b)
# reverse()函数 反向列表中的元素，仅支持列表
# m.reverse()
# print(m)
# sort() 函数，对数字排序，从小到大
# a=[2,6,5,8,9]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# 修改元素值 重新复制
# a[2]="haha"
# print(a)

# 列表排序
l=[5,6,8,1,0,4,6]
# 倒序一
l.sort(reverse=True)
print(l)
# 倒序二
res=sorted(l, reverse=True)
print(res)
# 倒序三
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j]<l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
