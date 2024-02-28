"""
    定义函数,根据生日(年月日),计算活了多天.
"""
import time

def get_birthday(year, month, day):
    # 参数　-> 字符串你
    str_time = "%s年%s月%s日" % (year, month, day)
    # 字符串　-> 时间元组
    tuple_time = time.strptime(str_time, "%Y年%m月%d日")
    # 当前时间戳 - 生日时间戳
    second = time.time() - time.mktime(tuple_time)
    return second / 60 / 60 / 24

print(get_birthday(2010, 1, 1)) # 4491.785878340056
# 截断删除
print("活了%d天" % get_birthday(2010, 1, 1))  # 4491
# 四舍五入
print("活了%.0f天" % get_birthday(2010, 1, 1))# 4492
