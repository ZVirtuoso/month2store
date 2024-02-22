"""
2.重构图书信息管理系统V3
    创建图书类
"""


class BookModel:
    """图书模型"""

    def __init__(self, name="", price=0.0, publishing=""):
        self.name = name
        self.price = price
        self.publishing = publishing

    def display(self):
        """显示"""
        print("%s的单价是%s,出版社是%s." % (self.name, self.price, self.publishing))


class BookController:
    def __init__(self):
        self.list_book = []  # type: list[BookModel]

    def add_book(self, book):
        self.list_book.append(book)

    pass


class BookView:
    def __init__(self):
        self.controller = BookController()

    def main(self):
        """功能入口"""
        while True:
            self.display_menu()
            self.select_menu()

    def display_menu(self):
        """显示菜单"""
        print("1键录入图书")
        print("2键查看图书")
        print("3键删除图书")
        print("4键修改图书")
        print("5键退出程序")

    def select_menu(self):
        """选择菜单"""
        number = input("请输入选项:")
        if number == "1":
            self.add_book()
        elif number == "2":
            self.show_all_book()
        elif number == "3":
            self.delete_book()
        elif number == "4":
            self.modify_book()
        elif number == "5":
            exit()

    def add_book(self):
        """添加图书"""
        book = BookModel(
            input("请输入书名:"),
            float(input("请输入单价:")),
            input("请输入出版社:")
        )
        self.controller.add_book(book)

    def show_all_book(self):
        """添加图书"""
        book = BookModel(
            input("请输入书名:"),
            float(input("请输入单价:")),
            input("请输入出版社:")
        )
        list_book.append(book)