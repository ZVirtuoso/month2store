"""
    文件读
"""
# 文件名,读取模式,编码方式
# file = open("demo01.py", "r", encoding="utf-8")
# try:
#     print(file.read())
# finally:
#     file.close()


with open("demo01.py", "r", encoding="utf-8") as file:
    # 读取文件中全部字符
    print(file.read())
    # 读取文件中指定字符
    # print(file.read(3))
    # 读取全部行
    # print(file.readlines())

# 离开with块后，文件一定自动关闭

# 每次读取一行,直到读取完毕
with open("demo01.py", "r", encoding="utf-8") as file:
    for item in file:
        print(item)

