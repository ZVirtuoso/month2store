"""
    自定义可迭代对象
"""
class MovieIterator: # 迭代器
    def __init__(self,data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        try:
            self.__index += 1
            return self.__data[self.__index]
        except IndexError:
            # return StopIteration # return 用于返回正确数据
            raise StopIteration # raise 用于发送错误消息

class MovieController: # 可迭代对象
    def __init__(self):
        self.list_movie = []
    def __iter__(self):
        return MovieIterator( self.list_movie)

controller = MovieController()
controller.list_movie.append("西游记")
controller.list_movie.append("八角笼中")
controller.list_movie.append("封神")
# for item in controller:
#     print(item)
iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration: # 接收错误
        break


list01= [10,20,30]
a = list01.__iter__()
print(a)
for item in list01:
    print(item)
b = list01.__iter__()
print(b)
for item in list01:
    print(item)