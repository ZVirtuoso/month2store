"""
    2. 遍历图书控制器

"""

class BookIterator:
    def __init__(self,data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        if self.__index >= len(self.__data) - 1:
            raise StopIteration
        self.__index += 1
        return self.__data[self.__index]

class BookController:
    def __init__(self):
        self.list_commodity = []

    def add_commodity(self,cmd):
        self.list_commodity.append(cmd)

    def __iter__(self):
        return BookIterator(self.list_commodity)

controller = BookController()
controller.add_commodity("Python入门到精通")
controller.add_commodity("Java入门到精通")
controller.add_commodity("C#入门到精通")
# 语法糖
# for item in controller:
#     print(item)
iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break