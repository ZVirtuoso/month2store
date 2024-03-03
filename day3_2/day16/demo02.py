"""
    排序
        降序：从大到小
    练习：
        升序：从小到大
"""
list01 = [5, 95, 6, 76, 87, 90]
# 复习：计算最大值算法(将结果存储在列表以外)
# max_value = list01[0]
# for i in range(1, len(list01)):
#     if max_value < list01[i]:
#         max_value = list01[i]
# print(max_value)

# 将列表第一个元素作为最大值
# 缺点：替换数据,造成旧数据丢失
# for i in range(1, len(list01)):
#     if list01[0] < list01[i]:
#         list01[0] = list01[i]
# print(list01) # [95, 95, 6, 76, 87, 90]

# 优化：使用交换
# for i in range(1, len(list01)):
#     if list01[0] < list01[i]:
#         list01[0], list01[i] = list01[i], list01[0]
# print(list01)  # [95, 5, 6, 76, 87, 90]
# 让第二个元素作为最大值
# for i in range(2, len(list01)):
#     if list01[1] < list01[i]:
#         list01[1], list01[i] = list01[i], list01[1]
# print(list01)  # [95, 90, 5, 6, 76, 87]
# 让第三个元素作为最大值
# for i in range(3, len(list01)):
#     if list01[2] < list01[i]:
#         list01[2], list01[i] = list01[i], list01[2]
# print(list01)  # [95, 90, 87, 5, 6, 76]


for r in range(len(list01) - 1):  # 取数据         0      1     2
    for c in range(r + 1, len(list01)):  # 作比较  12345  2345  345
        if list01[r] < list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
print(list01)  # [95, 90, 87, 76, 6, 5]








