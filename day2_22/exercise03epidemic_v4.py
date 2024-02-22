"""
MVC思想：
Model 模型,
View 视图,界面逻辑，负责输入输出
Controller 控制器,负责核心逻辑控制
"""

class EpidemicModel:
    def __init__(self, name, new=1, now=0):
        self.name = name
        self.new = new
        self.now = now


class EpidemicController:
    def __init__(self):
        self.list_table = []  # type: list[EpidemicModel]

    def add_info(self, epidemic):
        self.list_table.append(epidemic)

    def delete_epidemic(self, name):
        """删除疫情信息"""
        for i in range(len(self.list_table)):
            if self.list_table[i].name == name:
                del self.list_table[i]
                break

    def modify_epidemic(self, name, new, now):
        """修改疫情信息"""
        for item in self.list_table:
            if item.name == name:
                item.new = new
                item.now = now
                break


class EpidemicView:
    def __init__(self):
        self.controller = EpidemicController()

    def display_menu(self):
        """显示菜单"""
        print("输入1键录入疫情信息")
        print("输入2键显示疫情信息")
        print("输入3键删除疫情信息")
        print("输入4键修改疫情信息")
        print("输入5键退出程序")

    def select_menu(self):
        number = input("请输入选项:")
        if number == "1":
            self.input_epidemic()
        elif number == "2":
            self.display_epidemic()
        elif number == "3":
            self.delete_epidemic()
        elif number == "4":
            self.modify_epidemic()
        elif number == "5":
            exit()

    def input_epidemic(self):
        """输入疫情信息"""
        epidemic = EpidemicModel(name=input("请输入疫情名称:"),
                                 new=int(input("请输入新增确诊人数:")),
                                 now=int(input("请输入现有确诊人数:")), )
        self.controller.add_info(epidemic)

    def display_epidemic(self):
        for item in self.controller.list_table:
            print(f"{item.name}地区新增人数:{item.new},现有人数:{item.now}")

    def delete_epidemic(self):
        name = input("请输入疫情名称:")
        self.controller.delete_epidemic(name)

    def modify_epidemic(self):
        name = input("请输入需要修改的地区名:")
        new = int(input("请输入新增人数:"))
        now = int(input("请输入现有人数:"))
        self.controller.modify_epidemic(name, new, now)

    def main(self):
        while True:
            self.display_menu()
            self.select_menu()


view = EpidemicView()
view.main()
