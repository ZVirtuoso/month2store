class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money

    def __str__(self):
        return f"员工编号：{self.eid}, 部门编号：{self.did}, 姓名：{self.name}, 工资：{self.money}"


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "沙僧", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "沙僧", 15000),
]


def remove_employee_eid1003():
    for i, employee in enumerate(list_employees):
        if employee.eid == 1003:
            del list_employees[i]
# def remove_employee_name_sx():
#     for i in range(len(list_employees)-1,-1,-1):
#         if list_employees[i].name == '沙僧':
#             del list_employees[i]

def remove_employee_name_sx():
    for i ,item in enumerate(list_employees):
        if item.name == '沙僧':
            del list_employees[i]


def find_did_9001():
    for person in list_employees:
        if person.did == 9001:
            yield person


def find_name_len2():
    for person in list_employees:
        if len(person.name) == 2:
            yield person


def condition01(item):
    # 员工的did为9001
    return item.did == 9001


def condition02(item):
    # 员工的name的长度为2
    return len(item.name) == 2


def find_all_and(*conditions):
    # conditions为条件元组
    for person in list_employees:
        yield_mark = True
        for condition in conditions:
            if not condition(person):
                yield_mark = False
                break
        if yield_mark:
            yield person


# for employee in find_all_and(condition01):
#     print("满足条件1：", employee)
# for employee in find_all_and(condition02):
#     print("满足条件2：", employee)
# for employee in find_all_and(condition01, condition02):
#     print("满足条件1和2：", employee)


def sum_all_money():
    sum_money = 0
    for person in list_employees:
        sum_money += person.money
    return sum_money


def sum_all_eid():
    sum_eid = 0
    for person in list_employees:
        sum_eid += person.eid
    return sum_eid


if __name__ == '__main__':
    # print(sum_all_money())
    # print(sum_all_eid())
    #
    #
    # def conditon04(item):
    #     return item.money
    #
    #
    # print(IterableHelper.sum(list_employees, conditon04))

    remove_employee_name_sx()
    # remove_employee_eid1003()
    print(*list_employees,sep='\n')