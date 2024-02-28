from dtl import EmployeeModel


class EmployeeController:
    def __init__(self):
        self.list_employee = []

    def add_employee(self, new):
        self.list_employee.append(new)

    def remove_employee(self, name):
        try:
            self.list_employee.remove(EmployeeModel(name))
            return True
        except:
            return False

    def update_employee(self, model):
        for item in self.list_employee:
            if item.name == model.name:
                item.__dict__ = model.__dict__
                return True
        return False

