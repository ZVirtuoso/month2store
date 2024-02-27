from dtl import EmployeeModel


class EmployeeController:
    def __init__(self):
        self.list_table = []  # type:list[EmployeeModel]

    def add_employee(self, new):
        self.list_table.append(new)

    def remove_employee(self, name):
        target = EmployeeModel(name)
        if target in self.list_table:
            self.list_table.remove(target)
            return True
        return False
        # for i in range(len(self.list_table)):
        #     if self.list_table[i].name == name:
        #         del self.list_table[i]
        #         return True
        # return False

    def update_employee(self, model):
        for item in self.list_table:
            if item.name == model.name:
                item.__dict__ = model.__dict__
                return True
        return False