"""
练习1：定义函数,在列表中找出所有偶数
 [43,43,54,56,76,87,98]

练习2：定义函数,在列表中找出所有数字
 [43,"悟空",True,56,"八戒",87.5,98]
"""


def get_even(list_target):
    for item in list_target:
        if item % 2 == 0:
            yield item
# def get_number():
#     for item in list02:
#         if type(item) == int or type(item) == float:
#             yield item
def get_number():
    for item in list02:
        if type(item) in (int, float):
            # bool的父类是int，所以True是一种int,但True不是int
            # if isinstance(item, (int, float)):
            yield item


list01 = [43, 43, 54, 56, 76, 87, 98]
list02 = [43, "悟空", True, 56, "八戒", 87.5, 98]
res = get_even(list01)
for item in res:
    print(item)

for item in get_number():
    print(item)
