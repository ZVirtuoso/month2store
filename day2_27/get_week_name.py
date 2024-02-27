"""
    给定时间的年月日，返回星期数
    例：print(get_week_name(2020, 9, 15))# 星期二
"""
import time


def get_week_name(year, month, day):
    tuple_time = time.strptime(f'{year}-{month}-{day}', '%Y-%m-%d')
    index = tuple_time[-3]
    tuple_week = ('星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日',)
    return tuple_week[index]


if __name__ == '__main__':
    print(get_week_name(2020, 9, 15))
