"""
    文件管理
"""
from pathlib import Path

# 1. 创建
# 创建文件夹,如果已经存在则不再创建
Path("A").mkdir(exist_ok=True)

# 创建文件,如果已经存在则不再创建
Path("A/a.txt").touch()

# 2. 删除
# Path("A/a.txt").unlink(True) # 删除文件,如果不存在也不报错

# a_dir = Path("A")
# if a_dir.exists():
#     a_dir.rmdir() # 删除空文件夹

# 3. 重命名
Path("A").rename("B")
Path("B/a.txt").rename("B/b.txt")  # 注意:重命名后也需要带有路径
