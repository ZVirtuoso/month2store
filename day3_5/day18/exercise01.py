# 练习： 获取项目中所有python代码字符数

# 查找month01文件夹中都有哪些.py文件
from pathlib import Path

# for item in Path.cwd().parent.rglob("*.py"):
#     print(item)

total_len = 0
for item in Path("../").rglob("*.py"):
    # 统计每个文件的字数
    with open(item, "r", encoding="utf-8") as file:
        total_len += len(file.read())
print(total_len)
