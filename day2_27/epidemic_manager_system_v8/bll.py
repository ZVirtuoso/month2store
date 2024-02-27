from dtl import EpidemicModel


class EpidemicController:
    def __init__(self):
        self.list_table = []  # type: list[EpidemicModel]

    def add_info(self, epidemic):
        self.list_table.append(epidemic)

    def delete_epidemic(self, name):
        """删除疫情信息"""
        try:
            self.list_table.remove(EpidemicModel(name))
            return True
        except:
            return False
        # for i in range(len(self.list_table)):
        #     if self.list_table[i].name == name:
        #         del self.list_table[i]
        #         break

    def modify_epidemic(self, name, new, now):
        """修改疫情信息"""
        target = EpidemicModel(name, new, now)
        for i in range(len(self.list_table)):
            if self.list_table[i] == target:
                self.list_table[i] = target
                return True
        return False
