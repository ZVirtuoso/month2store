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
list_merge = [2, 2, 2, 2]

"""
def zero_to_end():
    # del list_merge[1] #  导致后面元素向前移动 [2, 0, 2]
    # del list_merge[2] # [2, 0]
    # del list_merge[2] # [2, 0,  2]
    # del list_merge[1] # [2, 2]

    # 结束值-1,不会包含,实际包含0
    for i in range(len(list_merge) - 1, -1, -1):
        print(list_merge[i])  # 3 2 1 0

    # 从最后一个元素开始到最后一个元素结束
    # for item in list_merge[len(list_merge) - 1: -1: -1]:
    #     print(item)

    # 会触发浅拷贝
    # for item in list_merge[:: -1]:
    #     print(item)
"""


def zero_to_end():
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            # del list_merge[i]
            # list_merge.remove(0) # 会再次循环查找为0的元素
            list_merge.append(0)

def merge():
    zero_to_end()  # 2 2 2 2
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]  # 4 4 0 0
            del list_merge[i + 1]
            list_merge.append(0)


merge()
print(list_merge)

# (选做)作业
# 3. 定义函数,将二维列表向左移动
# --将list_map每行赋值给list_merge
# --调用merge函数实现合并数据

# 4.定义函数,将二维列表向右移动
# --将list_map每行反转后赋值给list_merge
# --调用merge函数实现合并数据
# --再将list_merge还原给list_map

list_map = [
    [2, 0, 0, 2],
    [2, 2, 0, 0],
    [2, 0, 2, 0],
    [2, 8, 0, 4],
]

