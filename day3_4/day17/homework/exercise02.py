"""
    3. 为IterableHelper增加新功能:判断容器中是否包含重复元素
    需求：
        定义函数，判断餐厅列表中是否包含相同名称的餐厅name
        定义函数，判断餐厅列表中是否包含相同城市的餐厅city
        步骤：
           -- 根据需求，写出函数。
           -- 因为主体逻辑相同,核心算法不同.
              所以使用函数式编程思想(分、隔、做)
              创建通用函数
           -- 在当前模块中调用

"""


class RestaurantModel:  # 餐厅
    def __init__(self, name="", remark=0, city="北京", money=0.0):
        self.name = name
        self.remark = remark
        self.city = city
        self.money = money

    def __str__(self):
        return "餐厅名称:%s,人均消费:%s,城市:%s,总消费:%s" % (self.name, self.money, self.city, self.money)


list_restaurant = [
    RestaurantModel("北京饭店", 4, "北京", 132),
    RestaurantModel("上海饭店", 3, "上海", 142),
    RestaurantModel("南京饭店", 2, "广州", 121),
    RestaurantModel("苏州饭店", 0, "苏州", 96),
    RestaurantModel("广州饭店", 6, "广州", 100),
]

def is_repeat01():
    for r in range(len(list_restaurant) - 1):
        for c in range(r + 1, len(list_restaurant)):
            if list_restaurant[r].name == list_restaurant[c].name:
                return True
    return False

def is_repeat02():
    for r in range(len(list_restaurant) - 1):
        for c in range(r + 1, len(list_restaurant)):
            if list_restaurant[r].city == list_restaurant[c].city:
                return True
    return False

print(is_repeat02())


def is_repeat(condition):
    for r in range(len(list_restaurant) - 1):
        for c in range(r + 1, len(list_restaurant)):
            # if list_restaurant[r].city == list_restaurant[c].city:
            # if condition01(list_restaurant[r])==condition01(list_restaurant[c]):
            # if condition02(list_restaurant[r])==condition02(list_restaurant[c]):
            if condition(list_restaurant[r])==condition(list_restaurant[c]):
                return True
    return False


# def condition01(r,c):
#     return list_restaurant[r].city == list_restaurant[c].city

def condition01(item):
    return item.city

def condition02(item):
    return item.name


print(is_repeat(condition01))
print(is_repeat(lambda item:item.name))

