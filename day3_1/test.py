list_map = [[2, 0, 0, 2], [2, 2, 0, 0], [2, 0, 2, 0], [2, 8, 0, 4], ]
"""
    老师请问，如果.reverse()更省内存，那么放到推导式里面是不是同样省内存？
"""
list_map01 = [item[::-1] for item in list_map]
# 使用切片读取，没有改变原始列表
print("list_map=",list_map)
print("list_map01=",list_map01)
list_map02 = [item for item in list_map if not item.reverse()]
# 使用.reverse()，直接改变了原始列表，但更省内存
print("list_map=",list_map)
print("list_map02=",list_map02)
