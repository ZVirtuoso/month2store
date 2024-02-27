from dtl import EmployeeModel


class EmployeeController:
    def __init__(self):
        self.employee_list = []

    def add_employee(self, new_employee):
        if new_employee not in self.employee_list:
            self.employee_list.append(new_employee)
            return True
        else:
            return False

    def delete_employee(self, name):
        try:
            self.employee_list.remove(name)
            return True
        except ValueError:
            return False

    def update_employee(self, new_employee: EmployeeModel):
        for item in self.employee_list:
            if item.name == new_employee.name:
                item.__dict__ = new_employee.__dict__
                return True
        return False

    def find(self, name):
        if name in self.employee_list:
            return True
        else:
            return False


if __name__ == '__main__':
    controller = EmployeeController()
    controller.add_employee(EmployeeModel("John", "<EMAIL>"), 100)
    controller.find("John")
