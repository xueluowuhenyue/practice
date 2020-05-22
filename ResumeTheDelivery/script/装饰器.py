import time
# python装饰器（fuctional decorators）就是用于拓展原来函数功能的一种函数，
# 目的是在不改变原函数名(或类名)的情况下，给函数增加新的功能。
# 这个函数的特殊之处在于它的返回值也是一个函数，这个函数是内嵌“原“”函数的函数。

# def sub_time(pr_time):
#     def wrapper():
#         start_time = time.time()
#         pr_time()
#         end_time= time.time()
#         time_sub = end_time - start_time
#         print(time_sub)
#     return wrapper
#
#
# @sub_time
# def pr_time():
#     print("哈哈哈")
#     time.sleep(1)
#     # print(f"时间差是：{sub_time()}")
#     print("测试结束")

def sub(add):
    def sub_add(*args):
        print("hello")
        add(*args)
    return sub_add
@sub
def add(a,b):
    print(a+b)

@sub
def add2(a,b,c,d):
    print(a+b+c+d)


if __name__ == '__main__':
    # pr_time()
    add2(7, 3, 6, 5)