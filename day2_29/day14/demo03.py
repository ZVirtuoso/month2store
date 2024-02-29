"""
    内置生成器函数
        zip
            将多个可迭代对象中的元素合并为元组
"""
list_name = ["张无忌", "赵敏", "周芷若"]
list_room = [1001, 1002, 1003]
for item in zip(list_name, list_room):
    print(item)

# {'张无忌': 1001, '赵敏': 1002, '周芷若': 1003}
print(dict(zip(list_name, list_room)))
# print(dict([("猪", "八戒"), ("牛", "大圣")]))

list_map = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
# 矩阵转置
# [(1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15), (4, 8, 12, 16)]
# new_list = list(zip(list_map[0], list_map[1], list_map[2], list_map[3]))

# [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
# new_list = []
# for item in zip(list_map[0], list_map[1], list_map[2], list_map[3]):
#     new_list.append(list(item))
# print(new_list)

# new_list = [list(item) for item in zip(list_map[0], list_map[1], list_map[2], list_map[3])]
# print(new_list)

# 使用序列实参简化参数
new_list = [list(item) for item in zip(*list_map)]
print(new_list)

def func01(*args):
    pass

func01(1,2,3,4)
