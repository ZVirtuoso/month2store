"""
    3. (选做)2048核心算法
    # 全局变量
    list_merge = [2,0,0,2]
    # [2,0,0,2]  --> [2,2,0,0]
    # [2,2,0,0]  --> [2,2,0,0]
    # [2,0,2,0] -->  [2,2,0,0]
    # [2,8,0,4] -->  [2,8,4,0]
    # (1)定义函数,将零元素移至末尾
    # 思路：从后向前判断,如果为0删除,末尾追加0
"""
list_merge = [2, 0, 0, 2]

list_map = [
    [2, 4, 2, 2],
    [2, 2, 0, 0],
    [2, 0, 2, 0],
    [2, 8, 0, 4],
]

def move_right():
    global list_merge
    for item in list_map:  # [2, 4, 2, 2]
        list_merge = item[::-1]  # [2,2,4,2]
        merge()  # [4,4,2,0]
        item[::-1] = list_merge  # [0,2,4,4]


def move_left():
    global list_merge
    for item in list_map:
        list_merge = item
        merge()


def merge():
    zero_to_end()  # 2 2 0 0
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]  # 4 4 0 0
            del list_merge[i + 1]
            list_merge.append(0)


def zero_to_end():
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


move_left()
print(list_map)

# (选做)作业
# 5. 定义函数,将二维列表向上移动
# 矩阵转置
# 向左移动
# 矩阵转置

# 6.定义函数,将二维列表向下移动
# 矩阵转置
# 向右移动
# 矩阵转置