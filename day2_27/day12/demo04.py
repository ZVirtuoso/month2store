"""
    异常处理
        适用性:解决逻辑错误,而非语法错误
        异常现象:程序不再向下执行,而是不断返回
        核心价值:让程序能够按照既定流程执行
"""

# 语法错误
# NameError
# print(qtx)

# TypeError
# print(1 + "1")

# IndexError
# list01 = [10]
# print(list01[9])

# KeyError
# dict01 = {"a": 10}
# print(dict01["b"])

# 逻辑错误：往往因为数据超过预期范围而引发的错误
"""
def div_apple(apple_count): # 3
    # ValueError
    person_count = int(input("请输入人数:"))
    # ZeroDivisionError
    result = apple_count / person_count
    print("每人%s个苹果" % result)

def main():  # 2
    div_apple(10)


main() # 1
print("后续逻辑")
"""

# 对症下药(官方建议)
"""
def div_apple(apple_count): # 3
    try:
        # ValueError
        person_count = int(input("请输入人数:"))
        # ZeroDivisionError
        result = apple_count / person_count
        print("每人%s个苹果" % result)
    except ValueError:
        print("输入的不是整数")
    except ZeroDivisionError:
        print("人数不能为0")

div_apple(10)
print("后续逻辑")
"""

# 包治百病(民间喜爱)
def div_apple(apple_count):  # 3
    try:
        person_count = int(input("请输入人数:"))
        result = apple_count / person_count
        print("每人%s个苹果" % result)
    # except Exception:
    except:
        print("程序出错啦")


div_apple(10)
print("后续逻辑")

# 无论对错,一定执行的逻辑
"""
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数:"))
        result = apple_count / person_count
        print("每人%s个苹果" % result)
    finally:
        print("游戏结束")

div_apple(10)
print("后续逻辑")
"""