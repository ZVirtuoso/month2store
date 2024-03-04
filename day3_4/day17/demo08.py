"""
    搜索目录
"""
from pathlib import Path

month01 = Path.cwd().parent
# 搜索当前目录所有路径(一层)
# for item in month01.iterdir():
#     print(item)

# 根据通配符搜索当前目录所有路径(一层)，*表示任意多个字符
# for item in month01.glob("day1*"):
# for item in month01.glob("*/*/*"):
#     print(item)
# 根据通配符递归搜索当前目录所有路径(多层)
for item in month01.rglob("*.jpg"):
    print(item)



