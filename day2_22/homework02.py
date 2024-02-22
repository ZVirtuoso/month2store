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


class BookController:
    def __init__(self):
        self.list_book = []  # type: list[BookModel]

    def add_book(self, book):
        self.list_book.append(book)

    def delete_book(self, book_name):
        for i in range(len(self.list_book)):  # 0   1
            if self.list_book[i].name == book_name:
                del self.list_book[i]
                return True  # 必须停止,否则报错
        return False

    def modify_book(self, name, new_book):
        for item in self.list_book:
            if item.name == name:
                item.__dict__ = new_book.__dict__
                return True  # 建议停止,否则浪费性能

    def find_book_in_list(self, name):
        for item in self.list_book:
            if item.name == name:
                return True
        return False


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
        """展示所有图书"""
        for book in self.controller.list_book:
            print("%s的单价是%s,出版社是%s." % (book.name, book.price, book.publishing))

    def delete_book(self):
        """删除图书"""
        name = input("请输入需要删除的图书:")
        if self.controller.delete_book(name):
            print("成功删除")
        else:
            print("删除失败")

    def modify_book(self):
        name = input("请输入需要修改的图书名:")
        if self.controller.find_book_in_list(name):
            replace_book = BookModel(name=input("请输入新的图书名"),
                                     price=float(input("请输入新的单价")),
                                     publishing=input("请输入新的出版社"))
            if self.controller.modify_book(name, replace_book):
                print("修改成功")
        else:
            print("您输入的图书不存在")


view = BookView()
view.main()