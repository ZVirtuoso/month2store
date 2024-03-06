"""
    业务逻辑层
"""

from dtl import HouseModel
from dal import HouseDao


class HouseController:
    def __init__(self):
        self.__dao = HouseDao()
        self.__data_list = self.__dao.house_list  # type:list[HouseModel]

    def most_expensive_house(self):
        return max(self.__data_list)

    def smallest(self):
        return min(self.__data_list, key=lambda item: item.area)

    def get_all_house(self):
        return self.__data_list.__iter__()


# if __name__ == '__main__':
#     controller = HouseController()
#     print(list(item.community for item in controller.__data_list))
