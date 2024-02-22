"""
    电影信息管理系统V1-面向细节
        从终端录入数据，对电影(电影名、类型、演员、指数)进行增删改查
    电影信息管理系统V2-面向过程
        使用函数封装程序
    电影信息管理系统V3-封装数据
        创建Model类封装数据
    电影信息管理系统V4-面向对象
        使用MVC思想重构系统
            Model      模型:封装数据
            View       视图:处理界面逻辑,例如输入输出
            Controller 控制器:处理核心逻辑,例如存储计算
        餐厅架构
            服务员   <-传菜员->    厨师
    练习：完成MVC疫情信息管理系统
        删除、修改
    17：15 上课
"""


class MovieModel:
    def __init__(self, name="", type=(), actor="", index=0):
        self.name = name
        self.type = type
        self.actor = actor
        self.index = index


class MovieController:
    def __init__(self):
        self.list_table = []  # type:list[MovieModel]

    def add_movie(self, new):
        """
            添加电影
        :param new: 新电影
        """
        self.list_table.append(new)

    def delete_movie(self, name):
        """
            删除电影
        :param name: str类型,电影名称
        :return: bool类型,删除成功返回True,否则返回False
        """
        for i in range(len(self.list_table)):
            if self.list_table[i].name == name:
                del self.list_table[i]
                return True
        return False  # 删除失败

    def modify_movie(self, model: MovieModel):
        """
            修改电影
        :param model: MovieModel类型,需要修改的数据
        :return: bool类型,成功返回True,否则返回False
        """
        for item in self.list_table:
            if item.name == model.name:
                # item.type = model.type
                # item.actor =model.actor
                # item.index = model.index
                item.__dict__ = model.__dict__
                return True
        return False


class MovieView:
    def __init__(self):
        self.controller = MovieController()

    def display_menu(self):
        """显示菜单"""
        print("输入1键录入电影信息")
        print("输入2键显示电影信息")
        print("输入3键删除电影信息")
        print("输入4键修改电影信息")

    def select_menu(self):
        """选择菜单"""
        number = input("请输入选项:")
        if number == "1":
            self.input_movie()
        elif number == "2":
            self.display_movies()
        elif number == "3":
            self.remove_movie()
        elif number == "4":
            self.update_movie()

    def input_movie(self):
        """录入电影"""
        movie = MovieModel(
            input("请输入电影名称:"),
            tuple(input("请输入多个电影类型(-分割):").split("-")),
            input("请输入主要演员:"),
            int(input("请输入指数:")),
        )
        self.controller.add_movie(movie)

    def main(self):
        """程序入口"""
        while True:
            self.display_menu()
            self.select_menu()

    def display_movies(self):
        """显示所有电影"""
        for item in self.controller.list_table:
            print("%s的类型是%s,主演是%s,指数为%s" % (item.name, "-".join(item.type), item.actor, item.index))

    def remove_movie(self):
        while True:
            name = input("请输入需要删除的电影名:")
            if self.controller.delete_movie(name):
                print("删除电影成功")
                break
            else:
                print("删除电影失败")

    def update_movie(self):
        while True:
            movie = MovieModel(
                input("请输入电影名称:"),
                tuple(input("请输入多个电影类型(-分割):").split("-")),
                input("请输入主要演员:"),
                int(input("请输入指数:")),
            )
            if self.controller.modify_movie(movie):
                print("成功")
                break
            else:
                print("失败")


view = MovieView()  # -> controller -> []
view.main()  # main(view)
