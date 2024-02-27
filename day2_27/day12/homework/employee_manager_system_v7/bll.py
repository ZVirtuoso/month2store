from dtl import EmployeeModel


class EmployeeController:
    def __init__(self):
        self.list_table = []

    def add_employee(self, new):
        self.list_table.append(new)

    def remove_employee(self, name):
        target = EmployeeModel(name)
        if target in self.list_table:
            self.list_table.remove(target)
            return True
        return False

    def update_employee(self, model):
        for item in self.list_table:
            if item.name == model.name:
                item.__dict__ = model.__dict__
                return True
        return False


# 当前模块是主模块时,才执行测试代码
if __name__ == "__main__":
    controller = EmployeeController()
    controller.add_employee(EmployeeModel("张三", "java", 10000))
    controller.add_employee(EmployeeModel("张三", "java", 10000))
    controller.add_employee(EmployeeModel("张三", "java", 10000))
    for item in controller.list_table:
        print(item)
