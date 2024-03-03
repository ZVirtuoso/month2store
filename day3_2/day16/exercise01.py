"""
    需求：
        定义函数，查找工资最低的员工
        定义函数，查找编号最小的员工
        步骤：
           -- 根据需求，写出函数。
           -- 因为主体逻辑相同,核心算法不同.
              所以使用函数式编程思想(分、隔、做)
              创建通用函数get_min
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


def get_min01():
    min_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if min_value.money > list_employees[i].money:
            min_value = list_employees[i]
    return min_value


def get_min02():
    min_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if min_value.eid > list_employees[i].eid:
            min_value = list_employees[i]
    return min_value


print(get_min01())


def condition01(item):
    return item.eid


def condition02(item):
    return item.money


def get_min(condition):
    min_value = list_employees[0]
    for i in range(1, len(list_employees)):
        # if min_value.eid > list_employees[i].eid:
        # if condition01(min_value) > condition01(list_employees[i]):
        # if condition02(min_value) > condition02(list_employees[i]):
        if condition(min_value) > condition(list_employees[i]):
            min_value = list_employees[i]
    return min_value


print(get_min(condition02))
print(get_min(lambda element: element.money))

print(IterableHelper.get_min(list_employees, lambda element: element.money))
