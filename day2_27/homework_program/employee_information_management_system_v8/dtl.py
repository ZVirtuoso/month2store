class EmployeeModel:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"员工{self.name}的岗位是{self.position},工资为{self.salary}"

    def __eq__(self, value):
        if isinstance(value, EmployeeModel):
            return self.name == value.name
        if isinstance(value, str):
            return self.name == value

    def __gt__(self, other):
        return self.salary > other.salary


if __name__ == '__main__':
    emp1 = EmployeeModel("张三", "经理", 10000)
    emp2 = EmployeeModel("张三", "人事", 20000)
    # print(emp1 == emp2)# emp1.__eq__(emp2)
    # print(emp1 == "张三")
    print(emp1 < emp2)
