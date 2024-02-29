list_number = [56, 11231, 481, 13, 4, 16515, 12, 891, 45]


def get_number_odd():
    for number in list_number:
        if number % 2 == 1:
            return number


def get_number_div_3_5():
    for number in list_number:
        if number % 3 == 0 or number % 5 == 0:
            return number


def condition01(item):
    """判断是否为奇数"""
    return item % 2 == 1


def condition02(item):
    """判断是否为3的倍数"""
    return item % 3 == 0


def condition03(item):
    """判断是否为5的倍数"""
    return item % 5 == 0


def condition04(item):
    """判断是否为3或5的倍数"""
    return condition02(item) or condition03(item)


def get_number(condition):
    for number in list_number:
        if condition(number):
            return number


print(get_number(condition04))
