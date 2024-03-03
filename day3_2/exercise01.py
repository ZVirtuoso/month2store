from iterable_tools import IterableHelper as I


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money

    def __str__(self):
        return f"员工编号：{self.eid}, 部门编号：{self.did}, 姓名：{self.name}, 工资：{self.money}"


list_employees = [
    Employee(1001, 9002, "师父", 30000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

print(I.get_max(list_employees, lambda x: x.money))