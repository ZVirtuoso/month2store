"""
    时间模块
"""
import time

# 人类时间：2024年2月27日 11:13:10
# 时间元组类型(年,月,日,时,分,秒,星期,本年的天数,是否夏令时)
# time.struct_time
tuple_time = time.localtime()
print(tuple_time)
print(tuple_time[0])  # 年
print(tuple_time.tm_year)  # 年
print(tuple_time[-3])  # 星期
print(tuple_time.tm_wday)  # 星期
print(tuple_time[:3])  # (2024, 2, 27) 年月日
print(tuple_time[3:6])  # (11, 20, 55) 时分秒

# 时间戳:从1970年1月1日 00:00:00 到现在经过的秒数
print(time.time())  # 1709004645.6534257

# 时间元组 = time.localtime(时间戳)
print(time.localtime(1709004645.6534257))

# 时间戳 = time.mktime(元组)
print(time.mktime((1949, 10, 1, 0, 0, 0, 0, 0, 0)))
# 时间戳 = time.mktime(时间元组)
print(time.mktime(tuple_time))

# 格式化时间
# 字符串 = time.strftime("格式", 时间元组)
print(time.strftime("%y-%m-%d %H:%M:%S", tuple_time))
print(time.strftime("%Y年%m月%d日 %H时%M分%S秒", tuple_time))

# 2024年02月27日 11时45分24秒
# 时间元组 = time.strptime(字符串, 格式)
print(time.strptime("2024年 24秒", "%Y年 %S秒"))