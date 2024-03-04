"""
    外部函数作用域
"""


def func01():  # 外函数
    a = 10

    def func02():  # 内函数
        print(a)  # 内函数可以读取外函数变量

    # 内函数只能在外函数体内访问
    func02()


func01()


def func03():  # 外函数
    a = 10

    def func04():  # 内函数
        nonlocal a  # 内函数修改外函数变量前必须通过nonlocal声明
        a = 20

    func04()
    print(a)  # 20


func03()  #
