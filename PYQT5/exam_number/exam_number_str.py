"""
    判断八位数字
"""
while True:
    try:
        num = int(input("请输入八位数字"))

    except ValueError:
        print("输入的不是整数请重新输入")
    except Exception as e:
        print(type(e))
    else:
        if len(str(num)) != 8:
            print("输入的不是八位数，请重新输入")
        else:
            break
num = str(num)
result = 0
for i in range(1,9):
    if i % 2 != 0:
        result += int(num[-i])
    else:
        result += (int(num[-i]) * 2) // 10 + (int(num[-i]) * 2) % 10
if result % 10 == 0:
    print("是合法的银行卡号")
else:
    print("不是合法的银行卡号")

# result = sum([num // (10 * (index + 1)) for index in range(8) if not [].clear()])
# print(result)
