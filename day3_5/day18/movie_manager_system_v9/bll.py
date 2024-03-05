from dal import MovieDao
from dtl import MovieModel


class MovieController:
    def __init__(self):
        # self.list_table = []  # type:list[MovieModel]
        self.__dao = MovieDao()  # 加载历史数据
        self.list_table = self.__dao.list_target # type:list[MovieModel]

    def add_movie(self, new):
        """
            添加电影
        :param new: 新电影
        """
        self.list_table.append(new)
        self.__dao.save()

    def delete_movie(self, name):
        """
            删除电影
        :param name: str类型,电影名称
        :return: bool类型,删除成功返回True,否则返回False
        """
        try:
            self.list_table.remove(MovieModel(name))  # 如果电影不存在则报错
            self.__dao.save()
            return True
        except:
            return False

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
                self.__dao.save()
                return True
        return False
