"""
    内置高阶函数
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
# 1. 获取所有员工姓名
# 映射：将员工对象映射为员工姓名,类似于IterableHelper.select
for item in map(lambda item: item.name, list_employees):
    print(item)
# 2.获取部门是9002的所有员工
# 过滤:筛选出满足条件的元素，类似IterableHelper.find_all
for item in filter(lambda item: item.did == 9002, list_employees):
    print(item)
# 3. 获取最有钱/最穷的员工
print(max(list_employees, key=lambda item: item.money))
print(min(list_employees, key=lambda item: item.eid))
# 4. 列表排序方法
# -- 升序
list_employees.sort(key=lambda item: item.money)
# -- 降序
list_employees.sort(key=lambda item: item.money, reverse=True)
print(list_employees)
# 5. 排序函数
# -- 可以传入字典、元组等可迭代对象,但是一定返回新列表
print(sorted(list_employees,key=lambda item: item.money))
print(sorted(list_employees,key=lambda item: item.money, reverse=True))

