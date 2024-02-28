"""

"""


class MyRangeIterator:
    def __init__(self,stop):
        self.__number = -1
        self.__stop = stop
    def __next__(self):
        if self.__number == self.__stop - 1:
            raise StopIteration
        self.__number += 1
        return self.__number
class MyRange:
    def __init__(self, end):
        self.__end = end
    def __iter__(self):
        return MyRangeIterator(self.__end)

# 循环一次  计算一次  返回一次   只存当前不存之前
obj = MyRange(5)
iterator = obj.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)  # 0 1 2
    except StopIteration:
        break
