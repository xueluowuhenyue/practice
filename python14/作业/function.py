# -*- coding:utf-8 -*-
# 新手练习题：
#
# 1、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
# def judge(a):                                                             #定义一个函数，a为位置参数
#     if type(a) in (str,list,tuple):                                       #判断a是否是字符串、列表或元组
#         if len(a)>5:                                                      #判断a的长度
#             print('{}长度大于5，长度为{}'.format(a,len(a)))
#         elif len(a)<5:
#             print('{}长度小于5,长度为{}'.format(a,len(a)))
#         else:
#             print('{}长度等于5'.format(a))
#     else:
#         print('传入对象不符合要求，请重新输入！！！')
# judge({1,2,3,4})                                                                 #传入实参
# judge('cjghjkhk')                                                                #传入字符串
# judge([1,2,3])                                                                   #传入列表
# judge((9,8,5,6,1))                                                               #传入元组

# 2、写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
# def length(l):                                                   #定义函数，l为形参
#     if isinstance(l, list):                                      #判断l是否是列表
#         if len(l)>2:                                             #判断l的长度
#             print('前两个长度的内容是{}'.format(l[:2]))
#         else:
#             print('长度不足')
#     else:
#         print('请传入列表！！！')
# length([1,2])                                                   #传入实参
# length([1,2,3,4,5,6])
# length((1,2,3,4))                                               #传入元组
# length('djbjkcb')                                               #传入字符串

# 3、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典。
# def judge(d,s):                                                            #定义一个函数，d表示字典，s表示字符串
#     if isinstance(d, dict):                                                #判断d是否是字典
#         if isinstance(s, str):                                             #判断s是否是字符串
#             if s in d.values():                                            #判断字符串是否为字典中的
#                 print('字符串是为字典中的值')
#             else:
#                 ke=input('请输入key：')
#                 while True:
#                     if ke not in d.keys():                                #判断定义的键是否存在
#                         d[ke]=s                                           #在字典中插入数据
#                         print(d)
#                         break
#                     else:
#                         ke=input('key已经存在，请重新输入:')             #如果键存在则需要重新输入
#         else:
#             print('请传入一个字符串！！！')
#     else:
#         print('请传入一个字典')
# judge({'name':'df','age':'18岁'},'[5]')
# judge({'name':'df','age':'18岁'},'18岁')

# 4、一个足球队在寻找年龄在x岁到y岁的小女孩（包括x岁和y岁）加入。编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。
# def female_football(k,x=8,y=12):                              #定义函数及参数k,年龄默认8-12岁，k为询问次数
#     c=0                                                         #初始次数为0
#     sum=0                                                       #初始人数为0
#     while True:
#         c+=1
#         age=int(input('请输入你的年龄：'))                    #询问年龄
#         sex=input('请输入你的性别：')                         #询问性别
#         if x<=age<=y:                                         #判断年龄是否符合要求
#             if sex=='f':                                      #判断性别是否符合要求
#                 print('恭喜你可以加入女子足球队！！！')
#                 sum+=1
#             else:
#                 print('很遗憾你的性别不符合要求')
#         else:
#             print('很遗憾你的年龄不符合要求')
#         if c==k:                                              #当达到条件时终止统计
#             break
#     print('满足条件的人数有{}人'.format(sum))
# female_football(5)                                            #传入询问次数

# 进阶提升题：
#
# 1：利用字符串所学内置函数，完成如下题目，具体使用的函数已经提示过了~在课堂上，请去视频里面找答案！
# 请用自己目前所学实现指定字符串大写转小写，小写变大写，并且将字符串变为镜像字符串，镜像的意思是：大写的’A’变为’Z’,’大写的‘B‘变成‘Y,小写的’’’b’变为’y 。
# 目前要求处理的示范字符串是： ”sdSdsfdAdsdsdfsfdsdASDSDFDSFa” 需要提供至少2种不同的解决方法。
# s='sdSdsfdAdsdsdfsfdsdASDSDFDSFa'
# s1=''
# s=s.swapcase()                            #大小写转换
# for i in s:
#     if i.isupper():                       #判断是否是大写字母
#         i=chr(155-ord(i))                 #将大写字母转换成镜像字符
#         s1+=i
#     elif i.isdigit():                    #判断是否是数字
#         i=chr(155-ord(i))                 #将数字转换成镜像字符
#         s1+=i
#     else:
#         i=chr(219-ord(i))               #将小写字母转换成镜像字符
#         s1+=i
# print(s1)

# intable='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
# outtable='zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA0123456789'
# trantab=str.maketrans(intable,outtable)
# s1=s.swapcase()                                                          #大小写交换
# s2=s1.translate(trantab)
# print(s2)

# 2：搜索引擎中会对用户输入的数据进行处理，第一步就是词法分析，分离字符串中的数字、中文、拼音、符号。 比如这个字符串： 我的是名字是lemon,今年5岁。 语法分析后得到结果如下：
# 数字：5
# 中文：我的名字是、今年、岁
# 拼音：lemon
# 符号：，。 请编写程序实现该词法分析功能。
# s='我的是名字是Ajkghemon,今年5岁。'
# s1=''
# s2=''
# s3=''
# s4=''
# s5=''
# for i in s:
#     if i.isalpha():                                           #判断是否是字母
#         if u'\u4e00' <= i <= u'\u9fff':                       #判断是否是中文
#             s1+=i
#             s1+='、'
#         elif i.islower():                                     #判断是否是拼音
#             s2+=i
#             s2+='、'
#         else:                                                #判断是否是大写字母
#             s3+=i
#             s3+='、'
#     elif i.isdigit():                                        #判断是否是数字
#         s4+=i
#         s4+='、'
#     else:                                                    #其他符号
#         s5+=i
#         s5+='、'
# print('''拼音有：{}
# 大写字母有：{}
# 中文有：{}
# 数字有：{}
# 其他符号有：{}'''.format(s2.strip('、' ), s3.strip('、' ),s1.strip('、' ),s4.strip('、' ),s5.strip('、' )))

# s='我的名字是lemon,今年5岁。'
# s1=''
# s2=''
# s3=''
# s4=''
# s5=''
# for i in s:
#     if u'\u4e00' <= i <= u'\u9fff':                        #判断中文
#         s1+=i
#         s1+='、'
#     elif 48<=ord(i)<=57:                                  #判断数字
#         s2+=i
#         s2+='、'
#     elif 65<=ord(i)<=90:                                  #判断大写
#         s3+=i
#         s3+='、'
#     elif 97<=ord(i)<=122:                                  #判断小写
#         s4+=i
#         s4+='、'
#     else:                                               #判断符号
#         s5+=i
#         s5+='、'
# print('''拼音有：{}
# 大写字母有：{}
# 中文有：{}
# 数字有：{}
# 符号有：{}'''.format(s4.strip('、'), s3.strip('、'),s1.strip('、'),s2.strip('、'),s5.strip('、')))

