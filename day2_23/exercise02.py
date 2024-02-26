"""
重构内置函数
"""


class Movie:
    def __init__(self, name, index):
        self.name = name
        self.index = index

    def __add__(self, other):  # 要标注本类类型需用字符串。如果函数递归调用自己，其实并没有运行从而不会标红
        # 根据参数类型，选择不同的算法
        if type(other) is Movie:
            return Movie(self.name + other.name, self.index + other.index)
        if type(other) is int:
            return Movie(self.name, self.index + other)


m1 = Movie("封神", 100)
m2 = Movie("西游记", 200)
m3 = m1 + m2
print(m3.__dict__)
m4 = m1 + 10
print(m4.__dict__)
print(m1.__dict__)


def func01():
    func01()
