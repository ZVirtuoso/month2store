"""
    2. 图书信息管理系统V3
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


list_book = []  # type:list[BookModel]


def display_menu():
    """显示菜单"""
    print("1键录入图书")
    print("2键查看图书")
    print("3键删除图书")
    print("4键修改图书")


def add_book():
    """添加图书"""
    book = BookModel(
        input("请输入书名:"),
        float(input("请输入单价:")),
        input("请输入出版社:")
    )
    list_book.append(book)


def show_all_book():
    """显示所有图书"""
    for item in list_book:
        item.display()


def delete_book():
    """删除图书"""
    name = input("请输入需要删除的图书:")
    for i in range(len(list_book)):  # 0   1
        if list_book[i].name == name:
            del list_book[i]
            print("删除了" + name)
            break  # 必须停止,否则报错


def modify_book():
    """修改图书"""
    name = input("请输入需要修改的图书名:")
    for item in list_book:
        if item.name == name:
            item.name = input("请输入新的图书名")
            item.price = float(input("请输入新的单价"))
            item.publishing = input("请输入新的出版社")
            break  # 建议停止,否则浪费性能


def select_menu():
    number = input("请输入选项:")
    if number == "1":
        add_book()
    elif number == "2":
        show_all_book()
    elif number == "3":
        delete_book()
    elif number == "4":
        modify_book()


while True:
    display_menu()
    select_menu()
