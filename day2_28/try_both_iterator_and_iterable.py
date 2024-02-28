"""
    每次返回新创建的迭代器,才是主流做法
"""


class CommodityController():
    def __init__(self):
        self.model_list = []  # type: list[str]
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.__index += 1
            return self.model_list[self.__index]
        except:
            self.__index = -1  # 迭代结束重置索引值,可以下一次迭代
            raise StopIteration

    def add_model(self, new_model):
        self.model_list.append(new_model)


controller = CommodityController()
for item in ("金箍棒", "屠龙刀", "倚天剑", "芭比娃娃"):
    controller.add_model(item)
while True:  # 没有额外创建迭代器对象
    try:
        item = controller.__next__()
        print(item, end=' ')
    except StopIteration:
        print("使用while迭代结束")
        break
for item in controller:
    print(item, end=' ')
print("使用for迭代结束")
