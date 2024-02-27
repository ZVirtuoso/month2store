"""
创建字典，使用迭代思想，打印每个键值对
可迭代对象Iterable:具有__iter__()函数的对象
__iter__()返回迭代器对象
迭代器对象iterator: 具有__next__()函数的对象

"""
# 模拟for循环的原理:
dict_name = {"name": "小明", "age": 18, "sex": "男"}
# 1.创建迭代对象
iterator = dict_name.__iter__()
while True:
    try:
        # 2. 获取下一个元素
        key = iterator.__next__()
        print(key, dict_name[key])
    except StopIteration:# 3. 如果没有下一个元素了，就退出循环
        break
