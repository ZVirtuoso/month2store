from dtl import BookModel


class BookController:
    # list_book = []  # 类变量/全局变量
    def __init__(self):
        self.list_book = []  # type:list[BookModel]

    def delete_book(self, name):
        """删除图书"""
        target = BookModel(name)
        try:
            self.list_book.remove(target)
            return True
        except:
            return False

    def add_book(self, new):
        self.list_book.append(new)

    def modify_book(self, book: BookModel):
        """修改图书"""
        for item in self.list_book:
            if item.name == book.name:
                item.__dict__ = book.__dict__
                return True
        return False
