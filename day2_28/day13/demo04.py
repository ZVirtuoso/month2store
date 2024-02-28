"""
    生成器函数
        函数体中有yield
        用于产生海量数据,还几乎不占内存
        返回值是生成器对象
"""
"""
class MyRange:
    def __init__(self, end):
        self.__end = end
        
    def __iter__(self):
        number = 0
        while number <  self.__end  :
            yield number
            number += 1

obj = MyRange(5)
iterator = obj.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
"""



def my_range(end):
    number = 0
    while number < end:
        yield number
        number += 1

obj = my_range(5) # 不执行函数体,但返回生成器对象
iterator = obj.__iter__() # 不执行函数体,依然返回相同的生成器对象
while True:
    try:
        item = iterator.__next__() # 执行函数体,返回数据
        print(item)
    except StopIteration:
        break

"""
# 生成器伪代码
class generator: # 生成器
    def __iter__(self): # 可迭代对象
        return self
    
    def __next__(self): # 迭代器
        if 没有数据:
            raise StopInteration
        计算数据
        return 数据
"""