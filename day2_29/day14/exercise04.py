"""
练习1：使用生成器表达式在列表中获取所有字符串.

list01 = [43, "a", 5, True, 6, 7, 89, 9, "b"]

练习2：在列表中获取所有整数,并计算它的平方.
"""
list01 = [43, "a", 5, True, 6, 7, 89, 9, "b"]
# list_new = []
# for item in list01:
#     if type(item) == str:
#         list_new.append(item)
# print(list_new)

generator_new = (item for item in list01 if type(item) == str)
# ...
for item in generator_new:
    print(item)

generator_new = (item ** 2 for item in list01 if type(item) == int)
# ...
for item in generator_new:
    print(item)

