"""
    函数式编程重要理论支柱
        函数可以赋值给变量
"""
def func01():
    print("func01")

def func02():
    print("func02")

def func03(func):
    print("func03")
    # func02() # 直接调用
    func() # 间接调用

# a = func01() # 执行函数,将返回值None赋值给变量a
a = func01 # 不执行函数,将函数在代码区中的地址赋值给变量a
a() # 通过变量间接调用函数

# func03() # 函数func03固定搭配func02
func03(func02) # 函数func03搭配func02
func03(func01) # 函数func03搭配func01