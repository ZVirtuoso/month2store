"""
    函数参数
"""


def total_seconds(h=0, m=0, s=0):
    return h * 3600 + m * 60 + s


print(total_seconds(s=30))
print(total_seconds(m=2, s=30))
print(total_seconds(1, 2, 30))
print(total_seconds(1, s=30))
print(total_seconds(m=2))


def fun02(*p1):
    print(p1)


def multiplicative(*number_tuple):
    ans = 1
    for i in number_tuple:
        ans *= i
    return ans


print(multiplicative(2, 2, 2, 2, 3))


def fun03(*args, p1=0):  # 命名关键字形参，必须用关键字实参
    # 在星号元组形参之后，必须用关键字传参
    print(args)
    print(p1)


fun03(1, 2, 3, p1=1)


def fun04(*, p1=0):  # 强行使用命名关键字实参
    print(p1)


fun04(1, 2, 3, p1=3)


def fun05(p1, *, p2=0):  # 主次分明，前面的必须有，后面的次要
    print(p1)
    print(p2)

print()