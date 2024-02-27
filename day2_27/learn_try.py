"""
    异常处理:
        适用于 逻辑错误，而非语法错误
        触发后 程序不再向下执行，而是不断返回
        价值   让程序能够按照既定流程执行
"""


# 逻辑错误：
# 数据超过预期范围
def div_apple(apple_count):
    while True:
        try:
            person_count = int(input("请输入人数："))
            result = apple_count / person_count
            return f"每人{result:.2f}个苹果"

        except ValueError:
            print("输入有误，请输入整数")
        except ZeroDivisionError:
            print("人数不能为0")
        except:
            print("测试语句")
        finally:
            print("无论对错都执行的语句")


def main():
    return div_apple(10)


def get_score(chance):

    for i in range(chance):
        try:
            print("您有", chance-i, "次机会，请开始输入！")
            number = int(input("请输入数字:"))
            return number
        except ValueError:
            print("输入有误，请输入整数",end=",")
        finally:
            print("本次输入结束！")
    print("给你机会不中用啊！")
    return 0

print("您的得分是",get_score(5))
print("后续逻辑")
"""
创建函数，在终端中录入int类型成绩。如果格式不正确
"""