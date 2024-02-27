from bll import MovieController
from dtl import MovieModel


class MovieView:
    def __init__(self):
        self.__controller = MovieController()

    def __display_menu(self):
        """显示菜单"""
        print("输入1键录入电影信息")
        print("输入2键显示电影信息")
        print("输入3键删除电影信息")
        print("输入4键修改电影信息")

    def __select_menu(self):
        """选择菜单"""
        number = input("请输入选项:")
        if number == "1":
            self.__input_movie()
        elif number == "2":
            self.__display_movies()
        elif number == "3":
            self.__remove_movie()
        elif number == "4":
            self.__update_movie()

    def __get_number(self, message):
        while True:
            try:
                number = int(input(message))
                return number
            except:
                pass

    def __input_movie(self):
        """录入电影"""
        movie = MovieModel(
            input("请输入电影名称:"),
            tuple(input("请输入多个电影类型(-分割):").split("-")),
            input("请输入主要演员:"),
            self.__get_number("请输入指数:")
        )
        self.__controller.add_movie(movie)

    def main(self):
        """程序入口"""
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_movies(self):
        """显示所有电影"""
        for item in self.__controller.list_table:
            # print("%s的类型是%s,主演是%s,指数为%s" % (item.name, "-".join(item.type), item.actor, item.index))
            print(item)  # print(item.__str__())
            # 问题: 为什么在view类打印,去Model类重写?
            # 答：打印的对象类型是Model

    def __remove_movie(self):
        while True:
            name = input("请输入需要删除的电影名:")
            if self.__controller.delete_movie(name):
                print("删除电影成功")
                break
            else:
                print("删除电影失败")

    def __update_movie(self):
        while True:
            movie = MovieModel(
                input("请输入电影名称:"),
                tuple(input("请输入多个电影类型(-分割):").split("-")),
                input("请输入主要演员:"),
                self.__get_number("请输入指数:")
            )
            if self.__controller.modify_movie(movie):
                print("成功")
                break
            else:
                print("失败")
