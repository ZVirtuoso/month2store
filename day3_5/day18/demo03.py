"""
    文件写入
"""


# with open("data.txt","w",encoding="utf-8") as file:
#     file.write("你")
#     file.write("好")


class MovieModel:
    def __init__(self, name="", type=(), actor="", index=0):
        self.name = name
        self.type = type
        self.actor = actor
        self.index = index

    # 自定义对象->字符串(给人看的)
    def __str__(self):
        return "%s电影，主演：%s，类型：%s" % (self.name, self.actor, ",".join(self.type))

    # 自定义对象->字符串(给机器用的,必须满足Python语法)
    def __repr__(self):
        return 'MovieModel("%s",%s, "%s", %s)' % (self.name, self.type, self.actor, self.index)

# 1.内存中的Python对象
xyj = MovieModel("西游记", ("动作", "喜剧"), "黄晓明", 1)
print(xyj.name)

# 2.写入到文件中
with open("data.txt", "w", encoding="utf-8") as file:
    file.write(xyj.__repr__())

# 3.从文件中读取对象
with open("data.txt", "r", encoding="utf-8") as file:
    new = eval(file.read())
    print(new.name)


# list_movie = [
#     MovieModel("西游记",("动作", "喜剧"), "黄晓明", 1),
#     MovieModel("西游记",("动作", "喜剧"), "黄晓明", 1),
# ]
# print(list_movie[0]) # list_movie[0].__str__()
#
# print(list_movie) # list_movie.__repr__()内部会调用元素的__repr__

# 将字符串作为python代码执行
# print(eval("1+1"))
