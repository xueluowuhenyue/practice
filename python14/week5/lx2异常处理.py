# 1.try...except
# try:
#     print(a+2)
# except NameError as e:
#     print('错误：%s,已处理'%e) 

# 2.try...except..else 当try中代码正确时，执行else里的代码，否则不执行
# a=5
# try:
#     print(a+2)
# except NameError as e:
#     print('错误：%s,已处理'%e)
# else:
#     print(6)
    
# 3.try...except..finally 不管try中代码是否正确时，finally下的代码都会执行 
# try:
#     print(a+2)
#     resuit='成功'
# except NameError as e:
#     print('错误：%s,已处理'%e)
#     resuit='失败' 
# finally:
#     print(resuit)

# 4.raise 抛异常
# try:
#     print(a+2)
# except NameError as e:
#     print('错误：%s,已处理'%e) 
#     raise e

#5.try...except..finally&raise
# try:
#     print(a+2)
#     resuit='成功'
# except NameError as e:
#     print('错误：%s,已处理'%e)
#     resuit='失败' 
#     raise e
# finally:
#     print(resuit)

