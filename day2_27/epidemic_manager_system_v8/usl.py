"""
v8:新增异常处理
view针对所有int(input())代码进行封装
controller中remove如果报错则异常处理
"""
from bll import EpidemicController
from dtl import EpidemicModel


class EpidemicView:
    def __init__(self):
        self.__controller = EpidemicController()

    def __display_menu(self):
        """显示菜单"""
        print("输入1键录入疫情信息")
        print("输入2键显示疫情信息")
        print("输入3键删除疫情信息")
        print("输入4键修改疫情信息")
        print("输入5键退出程序")

    def __select_menu(self):
        number = input("请输入选项:")
        if number == "1":
            self.__input_epidemic()
        elif number == "2":
            self.__display_epidemic()
        elif number == "3":
            self.__delete_epidemic()
        elif number == "4":
            self.__modify_epidemic()
        elif number == "5":
            exit()

    def __get_int(self, message):
        while True:
            try:
                number = int(input(message))
                return number
            except ValueError:
                print("请重新输入整数!")

    def __input_epidemic(self):
        """输入疫情信息"""
        epidemic = EpidemicModel(name=input("请输入疫情名称:"),
                                 new=self.__get_int("请输入新增确诊人数:"),
                                 now=self.__get_int("请输入现有确诊人数:"), )
        self.__controller.add_info(epidemic)

    def __display_epidemic(self):
        for item in self.__controller.list_table:
            print(item)

    def __delete_epidemic(self):
        name = input("请输入疫情名称:")
        if self.__controller.delete_epidemic(name):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_epidemic(self):
        name = input("请输入需要修改的地区名:")
        new = self.__get_int("请输入新增人数:")
        now = self.__get_int("请输入现有人数:")
        if self.__controller.modify_epidemic(name, new, now):
            print("修改成功")
        else:
            print("修改失败")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()
