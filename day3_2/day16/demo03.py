"""
    降序排列-高阶函数
    练习：升序排列
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

    # def __gt__(self, other):
    #     return self.money > other.money
    #
    # def __gt__(self, other):
    #     return self.eid > other.eid


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]
# for r in range(len(list_employees) - 1):
#     for c in range(r + 1, len(list_employees)):
#         if list_employees[r].money < list_employees[c].money:
#             list_employees[r], list_employees[c] = list_employees[c], list_employees[r]
#
# for r in range(len(list_employees) - 1):
#     for c in range(r + 1, len(list_employees)):
#         if list_employees[r].eid < list_employees[c].eid:
#             list_employees[r], list_employees[c] = list_employees[c], list_employees[r]

# 违背了IterableHelper框架的使用习惯
# def condition01(r,c):
#     return list_employees[r].eid < list_employees[c].eid

def condition01(item):
    return item.eid

def condition02(item):
    return item.money

# for r in range(len(list_employees) - 1):
#     for c in range(r + 1, len(list_employees)):
#         # if list_employees[r].eid < list_employees[c].eid:
#         # if condition01(list_employees[r]) < condition01(list_employees[c]):
#         if condition02(list_employees[r]) < condition02(list_employees[c]):
#             list_employees[r], list_employees[c] = list_employees[c], list_employees[r]

def descending_order(condition):
    for r in range(len(list_employees) - 1):
        for c in range(r + 1, len(list_employees)):
            # if list_employees[r].eid < list_employees[c].eid:
            # if condition01(list_employees[r]) < condition01(list_employees[c]):
            # if condition02(list_employees[r]) < condition02(list_employees[c]):
            if condition(list_employees[r]) < condition(list_employees[c]):
                list_employees[r], list_employees[c] = list_employees[c], list_employees[r]

# descending_order(condition01)
descending_order(lambda item:item.did)
print(list_employees)




IterableHelper.descending_order(list_employees, lambda item:item.money)
print(list_employees)