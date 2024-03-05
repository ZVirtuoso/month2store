"""
    统计项目中所有python文件的字符数量
"""
from pathlib import Path

project_dir = Path("../")
characters_sum = 0
for py_file in project_dir.rglob("*.py"):
    with open(py_file, "r", encoding="utf-8") as file:
        characters_sum += len(file.read())
print(characters_sum)
