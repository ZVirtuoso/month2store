from dtl import EpidemicModel


class EpidemicController:
    def __init__(self):
        self.list_table = []  # type:list[EpidemicModel]

    def add_epidemic(self, new):
        """添加疫情信息"""
        self.list_table.append(new)

    def delete_epidemic(self, name):
        try:
            self.list_table.remove(name)
            return True
        except:
            return False

    def modify_epidemic(self, model: EpidemicModel):
        for item in self.list_table:
            if item.name == model.name:
                # item.new = model.new
                # item.now = model.now
                item.__dict__ = model.__dict__
                return True
        return False
