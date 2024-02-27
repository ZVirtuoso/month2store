"""
4. 定义函数,根据生日(年月日),计算活了多天.
输入：2010  1  1
输出：从2010年1月1日到现在总共活了3910天
公式：活的秒数：(当前时间戳-生日时间戳)
     换算为天数
"""
import time


def count_days(year, month, day):
    birth_str = f'{year}-{month}-{day}'  # 转化字符串
    birth_stamp = time.mktime(time.strptime(birth_str, "%Y-%m-%d"))  # 转换为时间元组，再转换为时间戳
    now_stamp = time.mktime(time.localtime())
    seconds = now_stamp - birth_stamp
    return seconds / 86400


if __name__ == '__main__':
    # print(time.mktime(time.strptime("2010-1-1", "%Y-%m-%d")))
    print("你活了%.2f天" % count_days(1998, 6, 17))
