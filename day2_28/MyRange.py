"""
    使用主流做法创建自定义range类
"""


class MyRangeIterator:
    def __init__(self,end):
        self.__end = end
        self.__index = -1

    def __next__(self):
        if self.__index < self.__end-1:
            self.__index += 1
            return self.__index
        else:
            raise StopIteration


class MyRange:
    def __init__(self,end):
        self.end = end

    def __iter__(self):
        return MyRangeIterator(self.end)


for number in MyRange(0):
    print(number)