class BookModel(object):
    """图书模型"""

    def __init__(self, name="", price=0.0, publishing=""):
        self.name = name
        self.price = price
        self.publishing = publishing

    def __str__(self):
        return f"书名:{self.name},价格:{self.price},出版社:{self.publishing}"

    # 重写快捷键ctrl+o
    def __eq__(self, o) -> bool:
        return self.name == o.name

    # def __eq__(self, other):
    #     return self.name == other.name


