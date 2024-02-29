"""
    生成器应用
        函数结果有多个,使用yield返回
        函数结果有一个,使用return返回
"""
list01 = [45, 54, 6, 7, 87, 8, 91, 0]


# 定义函数,将列表中大于50的数字取出
# 传统思想:创建容器,存储所有结果
def get_number_gt_50():
    list_number = []
    for item in list01:
        if item > 50:
            list_number.append(item)
    return list_number


data01 = get_number_gt_50()
print(data01)


# 生成器思想:使用yield生成结果
def get_number_gt_50():
    for item in list01:
        if item > 50:
            yield item

data01 = get_number_gt_50() # 不执行函数体,而是返回生成器对象
for item in data01:
    print(item)

# 11:22 上课
