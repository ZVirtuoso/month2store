"""
    数据访问层
"""
from dtl import HouseModel


class HouseDao:
    def __init__(self):
        self.house_list = self.load()  # type: list[HouseModel]

    # def save(self):
    #     with open("house.txt", "w", encoding="utf-8") as file:
    #         file.write(self.house_list.__repr__())

    def load(self):
        with open("house.txt", "r", encoding="utf-8") as file:
            return eval(file.read())


# if __name__ == '__main__':
#     house_dao = HouseDao()
#     print(list(item.community for item in house_dao.house_list))
