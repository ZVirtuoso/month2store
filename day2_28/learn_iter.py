"""
    可迭代对象
        __iter__() -> 迭代器

    迭代器
        __next__() -> 聚合对象元素
"""


class CommodityModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} 的售价为 {self.price} 元'


class CommodityIterator:
    def __init__(self, data):  # 我把init写成了int，一直提示创建实例时不能有参数，真的是蠢透了！
        self.__data = data
        self.__index = -1

    def __next__(self):
        if self.__index >= len(self.__data) - 1:
            raise StopIteration
        self.__index += 1
        return self.__data[self.__index].__str__()


class CommodityController(object):
    def __init__(self):
        self.model_list = []  # type: list[CommodityModel]

    def __iter__(self):
        return CommodityIterator(self.model_list)

    def add_model(self, new_model):
        self.model_list.append(new_model)


if __name__ == '__main__':
    controller = CommodityController()
    controller.add_model(CommodityModel(name='金箍棒', price=18))
    controller.add_model(CommodityModel(name='屠龙刀', price=19))
    controller.add_model(CommodityModel(name='芭比娃娃', price=20))
    controller.add_model(CommodityModel(name='《五年高考三年模拟》', price=21))

    # 使用for循环
    for model in controller:
        print(model)

    # 使用while循环
    # iterator = iterable_class.__iter__()
    # while True:
    #     try:
    #         item = iterator.__next__()
    #         print(item)
    #     except StopIteration:
    #         break
    # for item in zip(['五', '六', '七', '八'], iterable_class, [1, 2, 3, 4]):
    #     print(item)
