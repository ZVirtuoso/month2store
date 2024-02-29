"""
    生成器表达式
        语法上，将列表推导式的中括号改为小括号即可
        本质上，列表推导式存储所有数据
               生成器表达式只是生成器对象，使用数据时才开始计算存储当前数据
"""
list_number = [66, 25, 72, 86, 57]
list_new = [item for item in list_number if item > 60]
for item in list_new:
    print(item)

generator_new = (item for item in list_number if item > 60)
for item in generator_new:
    print(item)