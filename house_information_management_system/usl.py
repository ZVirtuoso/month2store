"""
    用户显示层
"""
from bll import HouseController
from dtl import HouseModel


class HouseView:
    def __init__(self):
        self.controller = HouseController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_oder()

    @staticmethod
    def __display_menu():
        print("1.显示房源信息")
        print("2.显示总价最贵的房源信息")
        print("3.显示面积最小的房源信息")
        print("4.保留选项")
        print("5.退出系统")

    def __select_oder(self):
        order = input("请输入指令序号：")
        if order == "1":
            self.__display_house()
        elif order == "2":
            self.__get_most_expensive_house()
        elif order == "3":
            self.__get_smallest_house()
        elif order == "4":
            pass
        elif order == "5":
            exit(0)
        else:
            print("输入不合法，请重新输入")

    # @staticmethod
    # def __input_int(message):
    #     while True:
    #         try:
    #             return int(input(message))
    #         except ValueError:
    #             print("输入不合法，请重新输入整数")
    #
    # @staticmethod
    # def __input_float(message):
    #     while True:
    #         try:
    #             return float(input(message))
    #         except ValueError:
    #             print("输入不合法，请重新输入数据")

    # def __input_house(self):
    #     new_house = HouseModel(
    #         id=self.__input_int("请输入房源编号："),
    #
    #         title=input("请输入房源标题："),
    #
    #         community=input("请输入小区名称："),
    #
    #         years=input("请输入房屋建造年份："),
    #
    #         house_type=input("请输入房屋类型："),
    #
    #         area=self.__input_float("请输入房屋面积："),
    #
    #         floor=input("请输入房屋楼层："),
    #
    #         description=input("请输入房屋描述信息："),
    #
    #         total_price=self.__input_float("请输入房屋总价："),
    #
    #         unit_price=self.__input_float("请输入房屋单价："),
    #
    #         follow_info=input("请输入房源跟进信息："),
    #     )

    def __display_house(self):
        for item in self.controller.get_all_house():
            print(item)

    def __get_most_expensive_house(self):
        result = self.controller.most_expensive_house()
        print("最贵的房源信息：" , result)

    def __get_smallest_house(self):
        result = self.controller.smallest()
        print("面积最小的房源信息：", result)


# if __name__ == "__main__":
#     view = HouseView()
#     view.main()
