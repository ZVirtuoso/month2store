"""
# (3) 练习：在month01目录中，分别使用相对路径、绝对路径判断下列文件是否存在：
# day03/demo01.py
# day03/homework/exercise01.py
# day04/homework/exercise01.py
"""
from pathlib import Path

print(Path("../day03/demo01.py").exists())
print(Path("../day03/homework/exercise01.py").exists())
print(Path("../day04/homework/exercise01.py").exists())

print(Path.cwd().parent.joinpath("day03/demo01.py").exists())
print(Path.cwd().parent.joinpath("day03/homework/exercise01.py").exists())
print(Path.cwd().parent.joinpath("day04/homework/exercise01.py").exists())
