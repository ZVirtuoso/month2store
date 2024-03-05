"""
    寻找项目中指定python文件
"""
from pathlib import Path


def find_special_py(str_find):
    read_count = 10
    for py_file in Path().cwd().parent.rglob("*.py"):
        with open(py_file, "r", encoding="utf-8") as file:
            if Path(py_file) != Path(__file__) and (index := (file_str := file.read()).find(str_find)) != -1:
                # 通过使用绝对路径判断是否是自己
                # file.read()类似生成器可迭代字符串，只能读取一次
                print(file.name)
                if not(index - read_count < 0 and index + read_count > len(file_str)):
                    print(file_str[index - read_count:index + read_count + 1])



# def condition01(file):
#     """
#         判断文件中是否包含定义函数wrapper来判断是否为闭包或装饰器练习
#     """
#     return "def wrapper(" in file.read()
#
#
# def condition02(file):
#     """
#         判断星号元组形参
#     """
#     return "(*" in file.read()

find_special_py("(*")
# print(Path().cwd().parent)
