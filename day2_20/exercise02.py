list_number = [4, 5, 6, 7, 8, 1, 9, 3]
# list_odd = []
# list_even = []  # 空列表的创建不可以同时创建
# for item in list_number:
#     if item % 2 != 0:
#         list_odd.append(item)
#     else:
#         list_even.append(item)
# print(list_odd)
# print(list_even)
list_odd = [item for item in list_number if item % 2]  # 和2取余有值
list_even = [item for item in list_number if not item % 2]  # 和2取余没有值
# 使用列表推导式更简洁，但两次循环性能更低
print(list_odd)
print(list_even)
