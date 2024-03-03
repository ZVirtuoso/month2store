"""
    升序排列
      小->大
"""
list01 = [43, 4, 5, 65, 76, 87, 9]
for r in range(len(list01) - 1):  # 1取数据
    for c in range(r + 1, len(list01)):  # 2作比较
        if list01[r] > list01[c]:  # 3找更小
            list01[r], list01[c] = list01[c], list01[r]  # 4则交换
print(list01)