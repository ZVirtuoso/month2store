"""
生成代码的大致逻辑
             1.将yield以前的代码定义在__next__函数中
             2.将yield后面的数据作为为__next__返回值

"""
from month02.day2_28.learn_iter import CommodityModel


class CommodityController(object):
    def __init__(self):
        self.model_list = []  # type: list[CommodityModel]

    def __iter__(self):
        for commodity in self.model_list:
            yield commodity
        # index = 0
        # yield self.model_list[index]
        # index += 1
        # yield self.model_list[index]
        # index += 1
        # yield self.model_list[index]
        # index += 1
        # yield self.model_list[index]


if __name__ == '__main__':
    controller = CommodityController()
    controller.model_list.append(CommodityModel(name='金箍棒', price=18))
    controller.model_list.append(CommodityModel(name='屠龙刀', price=19))
    controller.model_list.append(CommodityModel(name='芭比娃娃', price=20))
    controller.model_list.append(CommodityModel(name='《五年高考三年模拟》', price=21))

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
