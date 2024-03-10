"""
    判断八位数字
"""
import time

while True:
    try:
        num_input = int(input("请输入八位数字"))

    except ValueError:
        print("输入的不是整数请重新输入")
    except Exception as e:
        print(type(e))
    else:
        if len(str(num_input)) != 8:
            print("输入的不是八位数，请重新输入")
        else:
            break
time01 = time.process_time_ns()


def func1(num):
    result = 0
    for i in range(8):
        if i % 2 == 0:
            figure = (num // (10 ** i)) % 10
            result += figure
        else:
            figure = ((num // (10 ** i)) % 10) * 2
            figure = figure % 10 + figure // 10
            result += figure
    if result % 10 == 0:
        print("合法")
    else:
        print("不合法")


def func2(num):
    if (sum((num // (10 ** i)) % 10 for i in range(8) if i % 2 == 0) + sum(
            [(((num // (10 ** i)) % 10) * 2) % 10 + (((num // (10 ** i)) % 10) * 2) // 10 for i in range(8) if
             i % 2 != 0])) % 10 == 0:
        print("合法")
    else:
        print("不合法")


def func3(num):
    print('合法' if (sum((num // (10 ** i)) % 10 for i in range(8) if i % 2 == 0) + sum(
        [(((num // (10 ** i)) % 10) * 2) % 10 + (((num // (10 ** i)) % 10) * 2) // 10 for i in range(8) if
         i % 2 != 0])) % 10 == 0 else '不合法')

