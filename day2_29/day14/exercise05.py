"""
练习1：
    需求：
    定义函数，在列表中查找第一个奇数
    定义函数，在列表中查找第一个能被3或5整除的数字
    步骤：
    ​    -- 根据需求，写出函数。
    ​    -- 因为主体逻辑相同,核心算法不同.
    ​       所以使用函数式编程思想(分、隔、做)
    ​       创建通用函数find_single
    ​    -- 在当前模块中调用
"""
list01 = [0, 5, 6, 7, 8, 9]


def find_single01():
    for item in list01:
        if item % 2 != 0:
            return item
def find_single02():
    for item in list01:
        if item % 3 == 0 or item % 5 == 0:
            return item

# 1.
def condition01(item):
    return item % 2 != 0


def condition02(item):
    return item % 3 == 0 or item % 5 == 0


# 2.
def find_single(condition):
    for item in list01:
        # if condition02(item):
        # if condition01(item):
        if condition(item):
            return item

# 3.
re = find_single(   condition01  )
print(re)