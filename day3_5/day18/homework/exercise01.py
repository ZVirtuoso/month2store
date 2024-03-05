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
    RestaurantModel("上海饭店", 2, "南京", 121),
    RestaurantModel("苏州饭店", 0, "苏州", 96),
    RestaurantModel("广州饭店", 6, "苏州", 100),
]
for i in range(len(list_restaurant) - 1, -1, -1):
    if list_restaurant[i].city == "苏州":
        del list_restaurant[i]

for i in range(len(list_restaurant) - 1, -1, -1):
    if list_restaurant[i].name == "上海饭店":
        del list_restaurant[i]


def condition01(item):
    return item.city == "苏州"


def condition02(item):
    return item.name == "上海饭店"


def delete_all(condition):
    for i in range(len(list_restaurant) - 1, -1, -1):
        # if list_restaurant[i].name == "上海饭店":
        # if condition02(list_restaurant[i]):
        # if condition01(list_restaurant[i]):
        if condition(list_restaurant[i]):
            del list_restaurant[i]


delete_all(lambda item: item.name == "上海饭店")
