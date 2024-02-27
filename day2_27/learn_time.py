"""
    时间模块
"""
import time

# 人类时间2024年2月27日 11:13:30
# time.struct_time
# 时间元组类型(
#     0:年,
#     1:月,
#     2:日,
#     3:时,
#     4:分,
#     5:秒,
#     6:星期(从0索引),
#     7:本年天数(从1计算),
#     8:夏令时(1/0，是/否使用夏令时))
tuple_time = time.localtime()
print(tuple_time[:3])  # 年月日
print(tuple_time[3:6])  # 时分秒

##########################################
# 时间戳
#print(time.time())#1709005095.5642927

# 时间戳转换为时间元组
print(time.localtime(1709005095.5642927))

# 时间元组转换为时间戳
print(time.mktime((2024,6,17,0,0,0,0,0,0)))

# 格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S", tuple_time))

print(time.strptime("2024/6/17","%Y/%m/%d"))
print(time.strptime("6月3日 5时7分","%m月%d日 %H时%M分"))
