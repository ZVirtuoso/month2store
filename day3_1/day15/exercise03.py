"""
    需求：
        定义函数，获取所有员工姓名
        定义函数，获取所有员工编号与薪资
        步骤：
        ​    -- 根据需求，写出函数。
        ​    -- 因为主体逻辑相同,核心算法不同.
        ​       所以使用函数式编程思想(分、隔、做)
        ​       创建通用函数select
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
def select01():
    for item in list_employees:
        yield item.name

def select02():
    for item in list_employees:
        yield item.eid, item.money

def condition01(item):
    return item.name

def condition02(item):
    return item.eid, item.money

def select(condition):
    for item in list_employees:
        # yield item.eid, item.money
        # yield condition02(item)
        # yield condition01(item)
        yield condition(item)

for item in select(condition01):
    print(item)

# for item in select(lambda item:item.name):
for item in select(lambda item:(item.eid, item.money)):
    print(item)

for item in select01():
    print(item)

print(list(select02()))

print(list(IterableHelper.select(list_employees, lambda e: e.money > 20000)))