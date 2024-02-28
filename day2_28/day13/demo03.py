"""
    yield
"""


class MovieController:  # 可迭代对象
    def __init__(self):
        self.list_movie = []

    def __iter__(self):
        """
             生成代码的大致逻辑
             1.将yield以前的代码定义在__next__函数中
             2.将yield后面的数据作为为__next__返回值
        """
        index = 0
        yield self.list_movie[index]
        index += 1
        yield self.list_movie[index]
        index += 1
        yield self.list_movie[index]

controller = MovieController()
controller.list_movie.append("西游记")
controller.list_movie.append("八角笼中")
controller.list_movie.append("封神")
iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
