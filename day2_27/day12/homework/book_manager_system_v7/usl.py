from bll import BookController
from dtl import BookModel


class BookView:
    def __init__(self):
        self.__controller = BookController()

    def __display_menu(self):
        """显示菜单"""
        print("1键录入图书")
        print("2键查看图书")
        print("3键删除图书")
        print("4键修改图书")

    def __select_menu(self):
        number = input("请输入选项:")
        if number == "1":
            self.__input_book()
        elif number == "2":
            self.__show_all_book()
        elif number == "3":
            self.__remove_book()
        elif number == "4":
            self.__update_book()

    def __get_float(self, message):
        while True:
            try:
                result = float(input(message))
                return result
            except ValueError:
                print("数据类型错误，请重新输入数据！")

    def __input_book(self):
        """添加图书"""
        book = BookModel(
            input("请输入书名:"),
            self.__get_float("请输入单价:"),
            input("请输入出版社:")
        )
        self.__controller.add_book(book)

    def __show_all_book(self):
        """显示所有图书"""
        for item in self.__controller.list_book:
            # print("%s的单价是%s,出版社是%s." % (item.name, item.price, item.publishing))
            print(item)  # 因为打印的是model对象,所以会调用model的__str__方法

    def __update_book(self):
        while True:
            book = BookModel(
                input("请输入书名:"),
                self.__get_float("请输入单价:"),
                input("请输入出版社:")
            )
            if self.__controller.modify_book(book):
                print("成功")
                break
            else:
                print("失败")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __remove_book(self):
        while True:
            name = input("请输入需要删除的图书名:")
            if self.__controller.delete_book(name):
                print("成功")
                break
            else:
                print("失败")
