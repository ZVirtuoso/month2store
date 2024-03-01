from iterable_tools import IterableHelper

list01 = [43, 45, 65, 7, 9, 9]
dict_info = {"张三": 26, "李四": 24, "王五": 30, "赵六": 20, "钱七": 18}
dict_oooo = {"张三": 10, "李四": 100, "王五": "王五很富有"}
print("第一个奇数：", IterableHelper.find_single(list01, lambda num: num % 2 == 1))
print("所有小于10的数：", tuple(IterableHelper.find_all(list01, lambda num: num < 10)))
print("累加结果：", IterableHelper.sum(dict_info, lambda key: dict_info[key]))
print("第一个值是30的键名：", IterableHelper.find_single(dict_info, lambda key: dict_info[key] == 30))
print("所有值小于30的键名：", tuple(IterableHelper.find_all(dict_info, lambda key: dict_info[key] < 30)))
print("所有值小于30的键名：", tuple(IterableHelper.find_all(dict_oooo, lambda key: dict_info[key] < 30)))
