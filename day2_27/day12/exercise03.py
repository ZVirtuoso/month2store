"""
# 练习1：创建列表,使用迭代思想,打印每个元素.
# 练习2：创建字典,使用迭代思想,打印每个键值对.
"""
dict_info = {"name": "zhangsan", "age": 18, "sex": "男"}
iterator = dict_info.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key)
        print(dict_info[key])
    except StopIteration:
        break