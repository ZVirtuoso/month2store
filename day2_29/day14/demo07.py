"""
    函数时编程-应用
        适用性:
            多个函数主体结构相同,核心算法不同
        思想：
            将不同的核心算法单独定义为函数
            在通用函数中使用参数隔离核心算法

"""
list01 = [43, 45, 5, 6, 7, 8, 9]


# 定义函数,获取列表中第一个小于10的数字
def get_number_lt_10():
    for item in list01:
        if item < 10:
            return item

# 定义函数,获取列表中第一个个位是5的数字
def get_number_unit_5():
    for item in list01:
        if item % 10 == 5:
            return item


def condition01(item):
    return item < 10

def condition02(item):
    return item % 10 == 5

def get_number(condition):
    for item in list01:
        # if item < 10:
        # if condition01(item):
        # if condition02(item):
        if condition(item):
            return item

# 新增条件:
def condition03(item):
    # return item % 10 == 5 and item < 10
    return condition02(item) and condition01(item)

re1 = get_number(condition02)
re1 = get_number(condition03)
print(re1)