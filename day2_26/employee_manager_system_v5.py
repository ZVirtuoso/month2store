"""

"""


class EmployeeModel:
    def __init__(self, name="", job="", salary=0.0):
        self.name = name
        self.job = job
        self.salary = salary


class EmployeeController:
    def __init__(self):
        self.list_table = []  # type:list[EmployeeModel]

    def add_employee(self, new):
        self.list_table.append(new)

    def remove_employee(self, name):
        for i in range(len(self.list_table)):
            if self.list_table[i].name == name:
                del self.list_table[i]
                return True
        return False

    def update_employee(self, model):
        for item in self.list_table:
            if item.name == model.name:
                item.__dict__ = model.__dict__
                return True
        return False


class EmployeeView:
    def __init__(self):
        self.__controller = EmployeeController()

    def __input_employee(self):
        # 姓名、岗位、薪资
        model = EmployeeModel(
            name=input("请输入员工姓名:"),
            job=input("请输入员工岗位:"),
            salary=float(input("请输入员工薪资:"))
        )
        self.__controller.add_employee(model)

    def __display_menu(self):
        print("1. 添加员工")
        print("2. 删除员工")
        print("3. 修改员工")
        print("4. 显示员工")

    def __select_menu(self):
        menu = input("请输入您的选项(1-4):")
        if menu == "1":
            self.__input_employee()
        elif menu == "2":
            self.__display_employee()
        elif menu == "3":
            self.__delete_employee()
        elif menu == "4":
            self.__modify_employee()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_employee(self):
        for item in self.__controller.list_table:
            print("%s的岗位是%s,薪资%s元" % (item.name, item.job, item.salary))

    def __delete_employee(self):
        while True:
            name = input("请输入需要删除的员工姓名:")
            if self.__controller.remove_employee(name):
                print("删除成功")
                break
            else:
                print("删除失败")

    def __modify_employee(self):
        while True:
            model = EmployeeModel(
                name=input("请输入员工姓名:"),
                job=input("请输入员工岗位:"),
                salary=float(input("请输入员工薪资:"))
            )
            if self.__controller.update_employee(model):
                print("成功")
                break
            else:
                print("失败")


view = EmployeeView()
view.main()  # main(view)

# 10:15 上课