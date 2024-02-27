from bll import EmployeeController
from dtl import EmployeeModel


class EmployeeView:

    def __init__(self):
        self.__controller = EmployeeController()

    def __display_menu(self):
        print("1. 添加员工")
        print("2. 删除员工")
        print("3. 修改员工")
        print("4. 显示员工")

    def __select_menu(self):
        menu = input("请输入菜单序号：")
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

    def __input_employee(self):
        model = EmployeeModel(
            name=input("请输入员工姓名："),
            job=input("请输入员工岗位："),
            salary=float(input("请输入员工薪资："))
        )
        self.__controller.add_employee(model)

    def __display_employee(self):
        for item in self.__controller.list_table:
            print(item)

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
                name=input("请输入员工姓名："),
                job=input("请输入员工岗位："),
                salary=float(input("请输入员工薪资："))
            )
            if self.__controller.update_employee(model):
                print("修改成功")
                break
            else:
                print("修改失败")