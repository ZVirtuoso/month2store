from dtl import EpidemicModel


class EpidemicDao:
    def __init__(self):
        self.__file_name = 'data.txt'
        self.list_table = self.load()  # type: list[EpidemicModel]

    def save(self):
        with open(self.__file_name, "w", encoding="utf-8") as file:
            file.write(self.list_table.__repr__())

    def load(self):
        try:
            with open(self.__file_name, "r", encoding="utf-8") as file:
                return eval(file.read())
        except FileNotFoundError:
            return []
