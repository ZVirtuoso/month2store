"""
    迭代 iter ation:在之前的结果上进行重复的过程
    迭代器 iter ator:完成迭代过程的对象,具有__next__函数
    可迭代对象 iter able：创建迭代器,具有__iter__函数
"""
message = "我爱Python编程"
# for item in 100: # TypeError: 'int' object is not iterable
#     print(item)

# for循环原理
# 1. 创建迭代器对象
iterator = message.__iter__()
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()
        print(item)
    except StopIteration:  # 3. 如果没有下一个元素了，就退出循环
        break

# 笔试题：Python语言中,对象能够参与for循环的条件是什么？
# 答：对象具有__iter__函数，是可迭代对象

