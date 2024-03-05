"""
    文件读写
"""
# 文件名，读取模式，编码方式
# 创建文件对象
# file = open("file_manage.py", "r", encoding="utf-8")
# # 不写encoding会按照操作系统默认的编码（windows默认GBK，Linux默认utf-8）读取文件
# try:
#     print(file.read())
# finally:
#     file.close()

with open("file_manage.py", "r", encoding="utf-8") as file:
    file_str = file.read()
    print(file_str[0])
    # __n:指定读取字符数量，忽略则为全部
    # .read()返回一个字符串
    # 对于小文件，使用read()一次性读取所有内容最方便

    # print(file.readlines())
    # 读取全部的行，返回一个列表

    # for item in file:
    #     print(item)
    # 每次读取一行，最省内存

# 离开with语句块后，一定自动关闭文件，但是不会做异常处理
