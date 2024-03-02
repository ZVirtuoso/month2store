"""
    lambda 匿名函数
        lambda 参数:函数体
        lambda能表达的函数,def都能表达
        但是lambda不支持多条语句，且不能包含赋值语句
"""
# 1. 无参数无返回值
# def func01():
#     print('func01')
#
# func01()
func01 = lambda: print('func01')
func01()

# 2. 有参数有返回值
# def func02(p):
#     return p + 1
#
# re = func02(10)
# print(re)

func02 = lambda p: p + 1
re = func02(10)
print(re)

# 3. 有参数无返回值
# def func03(p1,p2):
#     print("参数是:",p1,p2)
#
# func03(10,20)

func03 = lambda p1, p2: print("参数是:", p1, p2)
func03(10, 20)

# 4. 无参数有返回值
# def func04():
#     return 10
#
# print(func04())

func04 = lambda: 10
print(func04())


# 5. 注意：lambda函数体只能有一条语句
def func05():
    for number in range(10):
        print(number)


func05()


# lambda :for number in range(10):
#     print(number)


# 6.lambda 函数体中不支持赋值语句
def func06(p):
    p[0] = 100


list01 = [10]
func06(list01)
print(list01)  # ?

# lambda p:p[0] = 100
