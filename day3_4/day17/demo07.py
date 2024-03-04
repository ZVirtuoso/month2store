"""
    路径信息
"""
from pathlib import Path

p1 = Path.cwd().joinpath("demo01.py")
print(p1)
print(p1.suffix)
print(p1.is_file())
print(p1.stat().st_size)
