"""
创建计算治愈比例的函数
"""


def rate_calculate(cure, confirmed):
    return 100 * cure / confirmed


confirmed = int(input("请输入确诊人数"))
cure = int(input("请输入治愈人数"))
rate = rate_calculate(cure, confirmed)
print("治愈比例为%.2f%%" % rate)

