# -*- coding:utf-8 -*-
import time,datetime

def update_time(str):
    '''这是一个时间转换函数'''
    #将时间转换成时间元组
    sw_time=time.strptime(str,"%Y-%m-%d %H:%M:%S")
    #转换成时间戳
    timeStamp=int(time.mktime(sw_time))
    return timeStamp
t1=update_time('2019-04-24 23:01:05')
nowTime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
# print(t3)
t2=update_time(nowTime)
# print(t2)
# print(t2-t1)

def judge_phone(str):
    p='(13|14|15|17|18)[0-9]{9}'
    if re.search(p,str)!=None:
        mn=re.search(p,str).group()
    else:
        mn='手机号码不符合规则'
    return mn

def update_time(str):
    '''这是一个时间转换函数'''
    #将时间转换成时间元组
    sw_time=time.strptime(str,"%Y-%m-%d %H:%M:%S")
    #转换成时间戳
    timeStamp=int(time.mktime(sw_time))
    return timeStamp