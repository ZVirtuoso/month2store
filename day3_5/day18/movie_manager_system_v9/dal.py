from dtl import MovieModel

class MovieDao:
    """
         电影数据访问类
    """

    def __init__(self):
        self.__file_name = "data.txt"
        self.list_target = self.load() # type:list[MovieModel]

    def save(self):
        """
            保存：列表 -> 文件
        """
        with open(self.__file_name, "w", encoding="utf-8") as file:
            file.write(self.list_target.__repr__())

    def load(self):
        """
            加载：文件 -> 列表
        """
        try:
            with open(self.__file_name, "r", encoding="utf-8") as file:
                return eval(file.read())
        except FileNotFoundError:
            return []
