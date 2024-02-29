"""
# 全局变量
list_merge = [2,0,0,2]
# [2,0,0,2]  --> [2,2,0,0]
# [2,2,0,0]  --> [2,2,0,0]
# [2,0,2,0] -->  [2,2,0,0]
# [2,8,0,4] -->  [2,8,4,0]
# (1)定义函数,将零元素移至末尾
# 思路：从后向前判断,如果为0删除,末尾追加0
# (2)定义函数,实现合并数据
# [2,2,0,0] --> [4,0,0,0]
# [2,2,2,0] --> [4,2,0,0]
# [2,0,2,0] --> [2,2,0,0]  -->  [4,0,0,0]
# 思路：先调用上面方法,从前向后判断相邻相同,
#      后元素累加到前元素,删除后元素,末尾追加0
"""


def move_zero(list_merge):
    # 定义函数,将零元素移至末尾,即向左滑
    # 使用负的索引需要从左往右删，删掉的0
    for i in range(-1, -len(list_merge) - 1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)
    return True


list_merge = [4, 0, 0, 2]
move_zero(list_merge)
print(list_merge)


def combine_same(list_merge):
    move_zero(list_merge)
    # 合并相同的相邻数据,仅做一次
    for i in range(3):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] *= 2
            del list_merge[i + 1]
            list_merge.append(0)


list_merge = [2, 0, 0, 2]
combine_same(list_merge)
print(list_merge)
