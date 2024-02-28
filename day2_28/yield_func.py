"""
生成器函数
    用于生成海量数据，还几乎不占内存
    返回值是生成器对象
        生成器是 迭代器 和 可迭代对象 的结合体

"""


def my_range(end):
    index = -1
    while index < end - 1:
        index += 1
        yield index


# for item in my_range(10):
#     print(item)
obj = my_range(10)
iterator = obj.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
