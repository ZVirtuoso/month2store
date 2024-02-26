"""
MVC思想：
Model 模型,
View 视图,界面逻辑，负责输入输出
Controller 控制器,负责核心逻辑控制
v5  view除了main函数，隐藏其他成员
v6  view直接打印Model，重写__str__
    controller直接remove删除，重写__eq__
"""


class EpidemicModel:
    def __init__(self, name, new=1, now=0):
        self.name = name
        self.new = new
        self.now = now

    def __str__(self):
        return f"{self.name}地区新增人数:{self.new},现有人数:{self.now}"

    def __eq__(self, other):
        return self.name == other.name


class EpidemicController:
    def __init__(self):
        self.list_table = []  # type: list[EpidemicModel]

    def add_info(self, epidemic):
        self.list_table.append(epidemic)

    def delete_epidemic(self, name):
        """删除疫情信息"""
        target = EpidemicModel(name)
        if target in self.list_table:
            self.list_table.remove(EpidemicModel(name))
            return True
        return False
        # for i in range(len(self.list_table)):
        #     if self.list_table[i].name == name:
        #         del self.list_table[i]
        #         break

    def modify_epidemic(self, name, new, now):
        """修改疫情信息"""
        target = EpidemicModel(name,new,now)
        for i in range(len(self.list_table)):
            if self.list_table[i] == target:
                self.list_table[i] = target
                return True
        return False


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

    def __input_epidemic(self):
        """输入疫情信息"""
        epidemic = EpidemicModel(name=input("请输入疫情名称:"),
                                 new=int(input("请输入新增确诊人数:")),
                                 now=int(input("请输入现有确诊人数:")), )
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
        new = int(input("请输入新增人数:"))
        now = int(input("请输入现有人数:"))
        if self.__controller.modify_epidemic(name, new, now):
            print("修改成功")
        else:
            print("修改失败")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()


view = EpidemicView()
view.main()
