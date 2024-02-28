"""
遍历图书控制器
"""


class BookIterator:
    def __init__(self,books):
        self.__books = books
        self.__index = -1
    def __next__(self):
        try:
            self.__index += 1
            return self.__books[self.__index]
        except:
            raise StopIteration


class BookController:
    def __init__(self):
        self.book_list = []

    def add_book(self, name):
        self.book_list.append(name)

    def __iter__(self):
        return BookIterator(self.book_list)


controller = BookController()
controller.add_book("Python入门到精通")
controller.add_book("Java入门到精通")
controller.add_book("C#入门到精通")

# for item in controller:
#     print(item)
iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break