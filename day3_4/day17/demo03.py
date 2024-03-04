"""
    闭包-应用-装饰器
        为"10年前的"旧功能增加新功能,但是不能修改函数体与调用端

        三大要素
            有外有内:延迟执行内函数代码
            内访问外:希望新旧功能同时执行
            外返回内:执行新旧功能的时机更灵活
"""
"""
def new_func():
    print("新功能")

def old_func():
    print("旧功能")

# 替换所有旧功能为新功能
old_func = new_func

old_func()
old_func()
old_func()
"""


"""
def new_func(func):
    print("新功能")
    func() #  执行旧功能

def old_func():
    print("旧功能")


old_func = new_func(old_func)

old_func()
old_func()
old_func()
"""


def new_func(func):
    def wrapper():
        print("新功能")
        func() #  执行旧功能
    return wrapper

def old_func():
    print("旧功能")


old_func = new_func(old_func)

old_func() # 拦截：调用内函数,而非调用旧功能
old_func()
old_func()