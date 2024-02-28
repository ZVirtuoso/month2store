"""
揉合了iterator和iterable的迭代器
"""


class MyRange(object):
    def __init__(self, end):
        self.__end = end
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < self.__end - 1:
            self.__index += 1
            return self.__index
        else:
            raise StopIteration


iterator = MyRange(5)
while True:
    try:
        item = iterator.__next__()
        print(item, end=' ')
    except StopIteration:
        print("使用while迭代结束")
        break

for i in MyRange(5):
    print(i, end=' ')
print("使用for迭代结束")
