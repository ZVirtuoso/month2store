"""
    需求：
        定义函数，根据薪资升序排列
        定义函数，根据编号升序排列
        步骤：
           -- 根据需求，写出函数。
           -- 因为主体逻辑相同,核心算法不同.
              所以使用函数式编程思想(分、隔、做)
              创建通用函数
           -- 在当前模块中调用
"""
from common.iterable_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money

    def __str__(self):
        return f"员工编号是{self.eid},部门编号是{self.did},员工姓名是{self.name},员工工资是{self.money}"


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]
for r in range(len(list_employees) - 1):
    for c in range(r + 1, len(list_employees)):
        if list_employees[r].money > list_employees[c].money:
            list_employees[r], list_employees[c] = list_employees[c], list_employees[r]

for r in range(len(list_employees) - 1):
    for c in range(r + 1, len(list_employees)):
        if list_employees[r].eid > list_employees[c].eid:
            list_employees[r], list_employees[c] = list_employees[c], list_employees[r]


def condition01(item):
    return item.money


def condition02(item):
    return item.eid


def ascending_order(condition):
    for r in range(len(list_employees) - 1):
        for c in range(r + 1, len(list_employees)):
            # if list_employees[r].eid > list_employees[c].eid:
            # if condition02(list_employees[r]) > condition02(list_employees[c]):
            if condition(list_employees[r]) > condition(list_employees[c]):
                list_employees[r], list_employees[c] = list_employees[c], list_employees[r]


ascending_order(lambda e: e.eid)

IterableHelper.ascending_order(list_employees, lambda e: e.eid)
print(list_employees)
