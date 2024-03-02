"""
    lambda 应用
        作为高阶函数的实参
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


def condition02(item):
    return item.money


def condition03(item):
    return item.money > 20000


# print(IterableHelper.sum(list_employees, condition02))
print(IterableHelper.sum(list_employees, lambda item: item.money))
# print(IterableHelper.find_single(list_employees, condition03))
print(IterableHelper.find_single(list_employees, lambda item: item.money > 20000))
