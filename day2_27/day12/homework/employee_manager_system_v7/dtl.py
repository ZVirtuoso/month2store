class EmployeeModel:
    def __init__(self, name="", job="", salary=0.0):
        self.name = name
        self.job = job
        self.salary = salary


    # 用于显示,当print时自动调用
    def __str__(self):
        return f"姓名：{self.name}职位：{self.job}薪资：{self.salary}"

    # 用于比较相同,当remove时自动调用
    def __eq__(self, o) -> bool:
        return self.name == o.name

    # 用于比较大小,当sort时自动调用
    def __gt__(self, other):
        return self.salary > other.salary

if __name__ == '__main__':
    model = EmployeeModel("张三", "经理", 10000)
    model = EmployeeModel("张三")
    print(model)
