"""
    生成器应用
    函数有多个结果，用yield返回多个结果
    函数只有一个结果，用return直接返回
"""
list01 = [45, 54, 6, 7, 87, 8, 81, 0]


# 取出大于50的数字
def get_number_gt_50():
    """
        传统思想：创建【容器】，存储所有结果
    """
    list_number = []
    for number in list01:
        if number > 50:
            list_number.append(number)
    return list_number


def get_number_gt_50_plus():
    """
        生成器思想：使用yield生成结果
            只存当前，不存之前
    """
    for number in list01:
        if number > 50:
            yield number

data = get_number_gt_50()
print(data)

for number in get_number_gt_50_plus():
    print(number)