"""
题目3：编写程序，计算列表中所有偶数的平均值
        list_number01 = [4, 5, 6, 7, 8, 1, 9, 3]
        list_number02 = [7, 5, 9, 7, 1]
"""
list_number01 = [4, 5, 6, 7, 8, 1, 9, 3]
list_number02 = [7, 5, 9, 7, 1]


def even_mean(list):
    """返回列表中所有偶数的平均值"""
    result = 0
    for item in list:
        if item % 2 == 0:
            result += item
    return result / len(list)


print(even_mean(list_number01))
print(even_mean(list_number02))
