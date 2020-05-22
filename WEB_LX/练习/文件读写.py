# -*- coding:utf-8 -*-
file=open(r'D:\pycharm-professional-2019.1.1\WEB_LX\data\file_read_write.txt',
          'a+',encoding='utf-8')

# 读取所有 按字节数读取
# print(file.read(30))
# 读取第一行n个字节 不填读取第一行数据
# print(file.readline())
# readlines()默认按行读取文件内容，返回列表，加for循环读取指定行


# def read_line(num1, num2=None):
#     if num2==None:
#         for line in file.readlines()[num1:]:
#             print(line)
#     else:
#         for line in file.readlines()[num1:num2]:
#             print(line)
#
#     return line
# write（）函数每次写数据都要清空  a表示追加
file.write('窗含西岭千秋雪')
# file.close()
file.seek(0,0)  # 移动光标 （0,0）移动到开头  第一个参数表示要移动多少个偏移量，
# 第二个参数表示从什么地方开始
print(file.read())
file.closed


# if __name__ == '__main__':
    # read_line(3)
    # read_line(5,8)