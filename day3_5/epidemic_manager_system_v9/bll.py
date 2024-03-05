from dtl import EpidemicModel
from dal import EpidemicDao


class EpidemicController:
    def __init__(self):
        self.__dao = EpidemicDao()
        self.list_table = self.__dao.list_table  # type: list[EpidemicModel]
        # 这里必须和内层dal的list_table指向同一列表
        # 如果在创建时选择load，则会产生两个不互通的列表对象

    def add_info(self, epidemic):
        self.list_table.append(epidemic)
        self.__dao.save()

    def delete_epidemic(self, name):
        """删除疫情信息"""
        try:
            self.list_table.remove(EpidemicModel(name))
            self.__dao.save()
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
                self.__dao.save()
                return True
        return False
