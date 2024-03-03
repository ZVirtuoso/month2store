"""
    最值
"""
from common.iterable_tools import IterableHelper

list01 = [43, 45, 6, 7, 89, 9, 0]


# 自定义算法，实现在列表中查找最大的数字
# max_value = list01[0]
# for i in range(1, len(list01)):
#     if max_value < list01[i]:
#         max_value = list01[i]
# print(max_value)


# ------------------------------------------
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


# max_value = list_employees[0]
# for i in range(1, len(list_employees)):
#     if max_value.money < list_employees[i].money:
#         max_value = list_employees[i]
# print(max_value)
#
# max_value = list_employees[0]
# for i in range(1, len(list_employees)):
#     if max_value.eid < list_employees[i].eid:
#         max_value = list_employees[i]
# print(max_value)

# 以下代码，打破了condition参数的习惯
# def get_max():
#     max_value = list_employees[0]
#     for i in range(1, len(list_employees)):
#         # if max_value.eid < list_employees[i].eid:
#         # if max_value.money < list_employees[i].money:
#         if condition01(max_value,i):
#             max_value = list_employees[i]
#     return max_value
#
# def condition01(max_value,i):
#     return max_value.eid < list_employees[i].eid

def get_max(condition):
    max_value = list_employees[0]
    for i in range(1, len(list_employees)):
        # if max_value.eid < list_employees[i].eid:
        # if max_value.money < list_employees[i].money:
        # if condition01(max_value)<condition01(list_employees[i]):
        # if condition02(max_value)<condition02(list_employees[i]):
        if condition(max_value) < condition(list_employees[i]):
            max_value = list_employees[i]
    return max_value


def condition01(item):
    return item.eid


def condition02(item):
    return item.money


print(get_max(condition01))
print(get_max(lambda e: e.did))

print(IterableHelper.get_max(list_employees, lambda e: e.money))
