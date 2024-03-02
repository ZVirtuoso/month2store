"""
    需求：
        定义函数，删除编号是1003的员工
        定义函数，姓名是"沙僧"的员工
        步骤：
        ​    -- 根据需求，写出函数。
        ​    -- 因为主体逻辑相同,核心算法不同.
        ​       所以使用函数式编程思想(分、隔、做)
        ​       创建通用函数delete_single
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

"""
# 定义函数,删除编号是1003的员工
def delete_single01():
    for i, item in enumerate(list_employees):
        if item.eid == 1003:
            del list_employees[i]
            return True
    return False

def delete_single02():
    for i, item in enumerate(list_employees):
        if item.name == "沙僧":
            del list_employees[i]
            return True
    return False

def condition01(item):
    return item.name == "沙僧"

def condition02(item):
    return item.eid == 1003

def delete_single(condition):
    for i, item in enumerate(list_employees):
        # if item.name == "沙僧":
        # if condition02(item):
        if condition(item):
            del list_employees[i]
            return True
    return False

print(delete_single(condition02))
"""

print(IterableHelper.delete_single(list_employees, lambda e: e.name == "孙悟空"))
