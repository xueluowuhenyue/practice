import time

# 获取当前时间
# print(time.localtime())

# 获取格式化的时间
# print(time.asctime(time.localtime(time.time())))

# 格式化日期
# 格式化成2020-02-28 16:10:29形式
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Fri Feb 28 16:02:02 2020形式
# print(time.strftime("%a %b %d %H:%m:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Fri Feb 28 16:02:09 2020"
print(time.mktime(time.strptime(a, "%a %b %d %H:%m:%S %Y")))