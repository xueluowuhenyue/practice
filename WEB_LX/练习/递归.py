# count=0
# for i in range(101):
#     for j in range(51):
#         for k in range(34):
#             if i+2*j+3*k==100:
#                 count+=1
# print(count)
# def  foo(n):
#     print(n)
#     n+=1
#     foo(n)
# foo(1)

#

# def age(n):
#     if n == 1:
#         return 18
#     else:
#         return age(n - 1) + 2
#
# ret=age(5)
# print(ret)

# 2.一个数，除2直到不能整除2
# def unm(a):
#     if a%2==0:
#         a=a//2
#         return unm(a)
#     else:
#         return a
# print(unm(4))

# 3.如果一个数可以整除2，就整除，不能整除就*3+1

# def func(num):
#     print(num)
#     if num==1:
#         return
#     elif num%2==0:
#         num=num//2
#     else:
#         num=num*3+1
#     func(num)
#
# func(5)

# def add(sum):
#     print(sum)
#     if sum ==1:
#         return 10
#     else:
#         return add(sum-1)+2
#
# print(add(3))

# 简单二分法
l = [2, 3, 5, 10, 15, 16, 18, 22, 26, 30, 32, 35, 41, 42, 43, 55, 56, 66, 67, 69, 72, 76, 82, 83, 88]
def find(l,aim):
    mid=len(l)//2               # 取中间值，//长度取整（取出来的是索引）
    if l[mid]>aim:              # 判断中间值和要找的那个值的大小关系
        new_l=l[:mid]           # 顾头不顾尾
        return find(new_l,aim)  # 递归算法中在每次函数调用的时候在前面加return
    elif l[mid]<aim:
        new_l=l[mid+1:]
        return find(new_l,aim)
    else:
        return l[mid]
print(find(l,66))


# 升级版二分法
def func(l, aim,start = 0,end = len(l)-1):
    mid = (start+end)//2#求中间的数
    if not l[start:end+1]:#如果你要找的数不在里面，就return'你查找的数字不在这个列表里面'
        return  '你查找的数字不在这个列表里面'
    elif aim > l[mid]:
        return func(l,aim,mid+1,end)
    elif aim < l[mid]:
        return func(l,aim,start,mid-1)
    elif aim == l[mid]:
        print("bingo")
        return mid


index = func(l,55)
print(index)
# print(func(l,41))


