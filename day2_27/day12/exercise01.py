"""
    练习1：定义函数,根据年月日,计算星期。
    输入：2020 9 15
    输出：星期二
"""
import time


def get_week_name(year, month, day):
    # year,month,day 拼接为字符串
    tuple_time = time.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
    # 星期数 = 时间元组[-3]
    index = tuple_time[-3]
    # 使用元组记录星期名
    tuple_week = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    return tuple_week[index]


name = get_week_name(2020, 9, 15)
print(name)
