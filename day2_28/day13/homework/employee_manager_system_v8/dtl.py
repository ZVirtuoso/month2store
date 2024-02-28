class EmployeeModel:
    def __init__(self, name="", job="", salary=""):
        self.name = name
        self.job = job
        self.salary = salary

    # 显示
    def __str__(self) -> str:
        return "%s岗位%s,薪资%s"%(self.name, self.job, self.salary)

    # 相同
    def __eq__(self, other) -> bool:
        return self.name == other.name

    # 大小
    def __gt__(self, other):
        return self.salary > other.salary



