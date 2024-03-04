"""
    当前文件demo06
    当前路径day17
"""
from pathlib import Path

# 使用相对路径
print(Path("./demo01.py").exists())
print(Path("./homework/exercise01.py").exists())
print(Path("../day16/demo01.py").exists())

# 使用绝对路径
# 当前路径
print(Path.cwd())
print(Path.cwd().joinpath("demo01.py").exists())
print(Path.cwd().joinpath("homework/exercise01.py").exists())
# print(Path.cwd().joinpath("../day16/demo01.py").exists())
print(Path.cwd().parent.joinpath("day16/demo01.py").exists())
