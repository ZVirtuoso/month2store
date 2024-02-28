from bll import EmployeeController
from dtl import EmployeeModel


class EmployeeView:
    def __init__(self):
        self.__controller = EmployeeController()

    def __display_menu(self):
        print("1.录入员工信息")
        print("2.显示员工信息")
        print("3.删除员工信息")
        print("4.修改员工信息")

    def __select_menu(self):
        number = input("请输入选项:")
        if number == "1":
            self.__input__employee()
        elif number == "2":
            self.__show_all_employee()
        elif number == "3":
            self.__remove_employee()
        elif number == "4":
            self.__update_employee()

    def main(self):
        """
            程序入口
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input__employee(self):
        model = EmployeeModel(
            name=input("请输入员工姓名:"),
            job=input("请输入员工岗位:"),
            salary=float(input("请输入员工薪资:"))
        )
        self.__controller.add_employee(model)

    def __show_all_employee(self):
        for item in self.__controller.list_employee:
            print(item) # 自动调用item.__str__()

    def __remove_employee(self):
        while True:
            name = input("请输入员工姓名:")
            if self.__controller.remove_employee(name):
                print("删除成功")
                break
            else:
                print("删除失败")

    def __update_employee(self):
        while True:
            model = EmployeeModel(
                name=input("请输入员工姓名:"),
                job=input("请输入员工岗位:"),
                salary=float(input("请输入员工薪资:"))
            )
            if self.__controller.update_employee(model):
                print("修改成功")
                break
            else:
                print("修改失败")





