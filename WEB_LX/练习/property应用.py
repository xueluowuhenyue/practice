# import json
# D='{"a":12,"B":15}'
# print(type(json.loads(D)))# 字符串转换成字典
#        
# m={"a":12,"B":15}
# print(type(json.dumps(m)))  # 字典转换成字符串


# python 装饰器
# def sub(add):
#     def wrapTheFunction(a,b):
#         return add(a,b)-8
#     return wrapTheFunction
# 
# @sub
# def add(a,b):
#     return a+b
# 
# print(add(5,6))

# python  property属性
class test:
    
    @property
    def add(self):
        a=5
        b=8
        return a+b
#         self.add
        
    def sub(self,d):    
        return self.add-d


class Parrot:
    def __init__(self, **kwargs):
        su = 0
        for i in kwargs.values():
            su += i
        self.__init__ = su

    @property
    def voltage(self):
        """Get the current voltage."""
        return self.__init__+6


print(Parrot(a=2, b=3, c=5).voltage)


if __name__ == '__main__':
    res=test().sub(3)
    print(res)
