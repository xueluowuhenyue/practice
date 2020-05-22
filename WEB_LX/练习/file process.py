# -*- coding:utf-8 -*-
# file:txt日志 不包括mp4、excel、html 处理读写
#  存储数据之读处理
# 第一步打开文件 open() file
# file=open('python1401',encoding='utf-8')
# print(file.read())  #默认读取所有内容，保持格式
# print(file.read(10))  #读取指定字符长度的内容
# print(file.readlines())  #按行读取读取所有行，返回列表，每行一个元素用逗号隔开
# print('*********************')
# content
# for i in range(10):          #读取前10行
#     print(file.readline())

# for i in range(10):          #读取前5-8行
#     if 5<=i<=8:
#         print(file.readline())
#     else:
#         file.readline()

# 文件之写处理
# 文件打开的模式 r,r+ 只读，读写
file=open('python1401.txt','w+',encoding='utf-8') # 清空文件

# print(file.readline())
# file.write('浔阳江')
# 先读后写写在后面，先写 覆盖写
# w,w+ 只写，读写
# file=open('python1401.txt','w+',encoding='utf-8') #清空文件
# file.write('哈哈哈哈哈')
# #file=open('python1401.txt','r',encoding='utf-8')#重新读
# file.seek(0,0)  #重新改变光标的位置  移动的量 相对位置 0开头【1当前位置，2尾部位置】
# print(file.read())
# file=open('python1401','r+',encoding='utf-8')
# ASCII编码 一个英文一个字节
# gbk 支持中文
# UTF-8编码 一个字符占三个字节
# ASCII-GBK  ascii-decode-utf-8-encode-gbk

# file=open('y.txt','w')  #文件不存在新建，存在清空在操作
# file.close()            #文件关闭

#  a,a+ 只能追加写，读写
file=open('python1402.txt','a',encoding='utf-8')  # 文件不存在新建在写
file.write('nxcbdvprbcx')
file.seek(0,0)
print(file.read())
# 写日志，生成html报告