"""
    装饰器 标准使用方式
"""


def new_func(func):  # 2
    def wrapper(*args):  # 4             合
        print("新功能")
        res = func(*args)  # 执行旧功能  # 5  拆
        return res

    return wrapper


@new_func  # old_func1 = new_func(old_func1)  # 1
def old_func1():
    print("旧功能1")


@new_func  # old_func2 = new_func(old_func2)  # 1
def old_func2(p1, p2, p3):  # 6
    print("旧功能2", p1, p2, p3)
    return 100


old_func1()  # 3
print(old_func2(10, 20, 30))  # 3
