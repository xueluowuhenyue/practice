# -*- coding:utf-8 -*-
import re
import random
from random import choice

# p='#(.*)#'
# s='xnkzkn#vcbvc#klcbnkv#'
# print(re.search(p,s).group())
# 获取手机号
# p='1(3|4|5|8|9)[0-9]{9}'  # 1(3|4|5|8|9)[0-9]{9} #0?(13|14|15|18|17)[0-9]{9}
# s='9566159846487658514'

# 获取邮箱
p='^(\d|[a-z])+@.[a-z]{3}'
s='5433kxb11fjdj@.sdfkg'
print(re.search(p,s).group())

# def create_phone():
#     # 第二位数字
#     second = [3, 4, 5, 7, 8][random.randint(0, 4)]
#     # 第三位数字
#     third = {
#     3: random.randint(0, 9),
#     4: [5, 7, 9][random.randint(0, 2)],
#     5: [i for i in range(10) if i != 4][random.randint(0, 8)],
#     7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
#     8: random.randint(0, 9),
#     }[second]
#     # 最后八位数字
#     suffix = random.randint(9999999,100000000)
#     # 拼接手机号
#     return "1{}{}{}".format(second, third, suffix)
#     # 生成手机号
#     phone = create_phone()
#     print(phone)
# # 正则
# reg = re.compile("(13\d|14[579]|15[^4\D]|17[^49\D]|18\d)\d{8}")
# print("Test passed!" if reg.match(phone) else "Test failed!")

for i in range(1,5):
    l = [3, 5, 7, 8, 9]
    s1=choice(l)
    s2=''
    s3=''
    if s1==3:
        s2=random.randint(0,9)
    elif s1==4:
        l=[5,7,9]
        s2 = choice(l)
    elif s1==5:
        l = [1,3,5,6,8,2,0, 7, 9]
        s2 = choice(l)
    else:
        l = [1, 3, 5, 6, 8, 2, 0, 7, 9,4]
        s2 = choice(l)
    for j in range(8):
        l = [1, 3, 5, 6, 8, 2, 0, 7, 9, 4]
        m= choice(l)
        s3+=str(m)
    print('第{}次结果是{}'.format(i,str(1)+str(s1)+str(s2)+s3))
    # print(str(1)+str(s1)+str(s2)+s3)

# p='#(.*?)#'
# str_1="{'mobilephone':'#mobilephone#','password':'#password#','memberid':'#memberid#'}"
# l=[18296208160,123456,12306]
# while True:
#     if re.search(p, str_1):
#         s = re.search(p, str_1).group(1)
#         for i in l:
#             value=str(i)
#             print(value)
#             str_2= re.sub(p, value, s)
# print(str_2)
