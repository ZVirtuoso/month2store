from dtl import EmployeeModel
from bll import EmployeeController


class EmployeeView:
    def __init__(self):
        self.__controller = EmployeeController()

    def __deploy_menu(self):
        print("1. 添加员工")
        print("2. 查询员工")
        print("3. 删除员工")
        print("4. 修改员工")
        print("5. 退出")

    def __select_menu(self):
        num = input("请输入指令(1~5):")
        if num == "1":
            self.__add_employee()
        if num == "2":
            self.__check_employee()
        if num == "3":
            self.__delete_employee()
        if num == "4":
            self.__update_employee()
        if num == "5":
            exit(0)

    def main(self):
        while True:
            self.__deploy_menu()
            self.__select_menu()

    def __get_float(self, message):
        pass

    def __add_employee(self):
        new_employee = EmployeeModel(
            name=input("请输入员工姓名:"),
            position=input("请输入员工职位:"),
            salary=float(input("请输入员工工资:")),
        )
        if self.__controller.add_employee(new_employee):
            print("添加成功")
        else:
            print("添加失败")

    def __check_employee(self):
        for item in self.__controller.employee_list:
            print(item)

    def __delete_employee(self):
        name = input("请输入要删除的员工姓名:")
        if self.__controller.delete_employee(name):
            print("删除成功")
        else:
            print("删除失败")

    def __update_employee(self):
        name = input("请输入员工姓名:")
        if not self.__controller.find(name):
            print("您输入的员工不存在")
        else:
            new_employee = EmployeeModel(
                name=name,
                position=input("请输入新的员工职位:"),
                salary=float(input("请输入新的员工工资:")),
            )
            if self.__controller.update_employee(new_employee):
                print("删除成功")
            else:
                print("删除失败")
