"""
    通过IterableHelper类实现下列功能：
        在list01中查找第一个奇数
        在list01中查找所有小于10的数字
        在dict_info中累加所有值
        在dict_info中查找第一个值是30的键名
        在dict_info中查找所有值小于30的键名
"""
from common.iterable_tools import IterableHelper

list01 = [43, 45, 65, 7, 9, 9]
dict_info = {
    "张三": 26, "李四": 24,
    "王五": 30, "赵六": 20, "钱七": 18
}


def condition01(item):  # 4
    return item % 2 == 1

def condition02(item):  # 4
    return item < 10


def condition04(item):
    return dict_info[item] == 30


def condition05(item):
    return dict_info[item] < 30


def condition03(item):  # 4
    return dict_info[item]


# print(IterableHelper.find_single(list01, condition01))
# print(list(IterableHelper.find_all(list01, condition02)))
# #                         1
# print(IterableHelper.sum(dict_info, condition03))
# print(tuple(IterableHelper.find_all(dict_info, condition05)))

print(IterableHelper.find_single(list01, lambda item:item % 2 == 1))
print(list(IterableHelper.find_all(list01, lambda item:item < 10)))
print(IterableHelper.sum(dict_info, lambda key:dict_info[key]))
print(tuple(IterableHelper.find_all(dict_info, lambda k:dict_info[k]<30)))


