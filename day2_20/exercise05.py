"""
    题目5：编写程序，统计平均年龄。
        list_person = [
            {"name": "张三", "age": 28},
            {"name": "李四", "age": 23},
            {"name": "王五", "age": 26},
        ]
    提示：遍历列表中每个元素
         取出年龄并累加到新变量
         最后用总年龄除以列表长度
"""
list_person = [
    {"name": "张三", "age": 28},
    {"name": "李四", "age": 23},
    {"name": "王五", "age": 26},
]
average_age = 0
for person in list_person:
    average_age += person["age"]
average = average_age / len(list_person)
print(average)