"""
    *(选做)彩票：双色球
    红色：6个  1--33之间的整数   不能重复
    蓝色：1个  1--16之间的整数
    1) 随机产生一注彩票(列表(前六个是红色，最后一个蓝色))
    2) 在终端中录入一支彩票
    要求：满足彩票的规则.
"""
import random
list_lottery = []
while len(list_lottery) < 6:
    random_number = random.randint(1,33)
    if random_number not in list_lottery:
        list_lottery.append(random_number)
list_lottery.append(random.randint(1,16))
print(list_lottery)

list_lottery_input = []
while len(list_lottery_input) < 6:
    input_number = int(input("请输入第"+str(1+len(list_lottery_input)) + "个红球编号"))
    if input_number not in range(1,34):
        print("编号错误请重新输入")
        continue
    elif input_number in list_lottery_input:
        print("编号重复，请重新输入")
        continue
    else:
        list_lottery_input.append(input_number)
while len(list_lottery_input) < 7:
    blue_number = int(input("请输入蓝球编号"))
    if blue_number not in range(1,17):
        print("编号错误请重新输入")
    else:
        list_lottery_input.append(blue_number)
print(list_lottery_input)
