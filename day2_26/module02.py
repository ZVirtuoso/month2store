# import module01
# # 我过去使用全局变量、函数、类与成员
# print(module01.data)
# temp = module01.MyClass()
# temp.func02()
# module01.func01()

# 你过来
from module01 import data as dataa
print(dataa)
from module01 import func01 as MyClass
MyClass()
from module01 import MyClass as OurClass
temp = OurClass()
temp.func02()