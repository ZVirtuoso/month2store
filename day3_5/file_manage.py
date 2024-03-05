"""
    文件管理
"""
from pathlib import Path

# 增
Path("A").mkdir(exist_ok=True)
Path("A/a.txt").touch()

# # 删
# Path("A/a.txt").unlink(True)
# # 没有上层目录却删：FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'A\\a.txt'
# # unlink(True)表示若文件不存在则忽略
#
# Path("A").rmdir()
# # 删除文件夹，如果文件夹非空则报错 OSError: [WinError 145] 目录不是空的。: 'A'
# # 如果文件夹不存在 FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'A'
# # 所以最好配合if Path("A").exists()或者try语句实现文件夹删除

# 改（重命名）
# 若新名字已存在则报错 FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: 'A' -> 'B'
if not Path("B").exists():Path("A").rename("B")
Path("A/a.txt").rename("b.txt")

