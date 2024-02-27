"""
    练习：创建函数，在终端中录入int类型成绩。如果格式不正确，重新输入。
    效果： score = get_score()
     print("成绩是：%d"%score)
"""


def get_score():
    while True:
        try:
            number = int(input("请输入数字:"))
            return number  # 退出函数(能执行到本行,上一行肯定没错)
        except:
            pass


print(get_score())
