"""
    内置生成器函数enumerate
"""
list01 = [45, 45, 6, 7, 8]
# 根据条件读元素
for item in list01:
    if item > 40:
        print(item)
# 根据条件改元素
for i in range(len(list01)):
    if list01[i] > 40:
        list01[i] = 40
# 根据条件读+改元素
# 元组(索引,元素)
# for item in enumerate(list01):
#     print(item)
for i, item in enumerate(list01):
    if item > 40:
        list01[i] = 40
