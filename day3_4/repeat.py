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
    RestaurantModel("苏州饭店", 0, "上海", 96),
    RestaurantModel("广州饭店", 6, "广州", 100),
]


def is_repeat(iterable,handler):
    dict_new = {}
    repeat_key = []
    for i,item in enumerate(iterable):
        if handler(item) not in dict_new:
            dict_new[handler(item)] = [i]
        else:
            dict_new[handler(item)].append(i)
            repeat_key.append(handler(item))

    return {key:dict_new[key] for key in repeat_key}



print(is_repeat(list_restaurant,lambda item:item.city))
