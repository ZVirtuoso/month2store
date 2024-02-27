class EmployeeModel:
    def __init__(self, name="", job="", salary=0.0):
        self.name = name
        self.job = job
        self.salary = salary

    def __str__(self):
        return f"姓名：{self.name}，岗位：{self.job}，薪资：{self.salary}"

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.salary > other.salary
