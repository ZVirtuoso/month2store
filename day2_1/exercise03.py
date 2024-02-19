"""
根据月日,计算是这一年的第几天.
公式：前几个月总天数 + 当月天数 例如：5月10日
计算：31 29 31 30 + 10
"""
tuple_days = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = int(input("请输入月份"))
day = int(input("请输入日期"))
if month not in range(1, 13) \
        or day not in range(1, tuple_days[month]):
    print("日期输入有误")
else:
    sum_days = sum(tuple_days[:month - 1]) + day
    print("总天数是" + str(sum_days))

# print(str(tuple_days))
