"""
    列表与生成器对比
        列表
            优点
                反复使用
                支持索引切片
            缺点
                占用内存较多
        生成器
            优点
                即使生成海量数据,也几乎不占内存
            缺点
                一个生成器对象只能使用一次
                不支持索引切片
            适用性
                函数返回多个结果使用生成器函数yield
                建议将列表推导式写成生成器表达式
            解决
                转换为容器
"""
list01 = [5,45,65,76,87,9]
def get_number_gt_50():
    for item in list01:
        if item > 50:
            yield item

data01 = list(get_number_gt_50())
print(data01[-1])
for item in data01:
    print(item)
# for item in data01:
#     print(item)
