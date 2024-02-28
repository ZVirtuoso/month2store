"""
    非主流做法：
        可迭代对象 + 迭代器
"""

class MovieController:
    def __init__(self):
        self.list_movie = []
        self.__index = -1

    def __iter__(self):# 可迭代对象
        return self

    def __next__(self):# 迭代器
        try:
            self.__index += 1
            return self.list_movie[self.__index]
        except IndexError:
            raise StopIteration  # raise 用于发送错误消息

controller = MovieController()
controller.list_movie.append("西游记")
controller.list_movie.append("八角笼中")
controller.list_movie.append("封神")
# for item in controller:
#     print(item)
# for item in controller:
#     print(item)
iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
iterator = controller.__iter__() # 返回旧
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break