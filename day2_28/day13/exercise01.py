"""

"""


class CommodityIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        try:
            self.__index += 1
            return self.__data[self.__index]
        except:
            raise


class CommodityController:
    def __init__(self):
        self.list_commodity = []

    def add_commodity(self, cmd):
        self.list_commodity.append(cmd)

    def __iter__(self):
        return CommodityIterator(self.list_commodity)


controller = CommodityController()
controller.add_commodity("屠龙刀")
controller.add_commodity("倚天剑")
controller.add_commodity("芭比娃娃")

iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
