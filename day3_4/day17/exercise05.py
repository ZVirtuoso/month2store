import time

# 练习：
# -- 打印所有图片的大小
from pathlib import Path

# for item in Path.cwd().parent.rglob("*.jpg"):
#     print(item.stat().st_size)

# list_size = []
# for item in Path.cwd().parent.rglob("*.jpg"):
#     list_size.append(item.stat().st_size)
# print(list_size)

list_size = [item.stat().st_size for item in Path.cwd().parent.rglob("*.jpg")]
print(list_size)

print(list(map(lambda item: item.stat().st_size, Path.cwd().parent.rglob("*.jpg"))))

# 打印day03中所有练习的路径
# for item in Path.cwd().parent.glob("day03/e*"):
#     print(item)

# 打印所有文本(.txt)文件的创建时间(格式：年/月/日)
for item in Path.cwd().parent.rglob("*.txt"):
    print(time.localtime(item.stat().st_ctime)[:3])
