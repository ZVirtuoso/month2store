"""
2. 使用IterableHelper类实现下列功能：
      class BookModel:
        def __init__(self, name="", price=0.0, publishing=""):
            self.name = name
            self.price = price
            self.publishing = publishing

      list_book = [
          BookModel("Python", 56.0, "铁道部出版社"),
          BookModel("Java", 47.0, "清华大学出版社"),
          BookModel("C++", 66.0, "清华大学出版社"),
          BookModel("C", 32.0, "铁道出版社"),
          BookModel("JavaScript", 40.0, "清华大学出版社"),
      ]
      2.1获取列表中所有图书的名称
      2.2获取列表中价格大于50元的图书
      2.3删除列表中图书名"Python"的图书
      2.4累加所有图书价格
      2.5获取名称为“JavaScript”的图书


      class RestaurantModel: # 餐厅
        def __init__(self, name="", remark=0, city="北京", money=0.0):
            self.name = name
            self.remark = remark
            self.city = city
            self.money = money

      list_restaurant = [
            RestaurantModel("北京饭店", 4, "北京", 132),
            RestaurantModel("上海饭店", 3, "上海", 142),
            RestaurantModel("南京饭店", 2, "南京", 121),
            RestaurantModel("苏州饭店", 0, "苏州", 96),
            RestaurantModel("广州饭店", 6, "广州", 100),
      ]
      2.6获取列表中所有餐厅的名称与人均消费
      2.7删除列表中"广州饭店"
      2.8累加所有餐厅的人均消费
      2.9获取列表中点评人数不为0的餐厅
      2.10获取名称为“上海饭店”的餐厅
"""

from common.iterable_tools import IterableHelper


class BookModel:
    def __init__(self, name="", price=0.0, publishing=""):
        self.name = name
        self.price = price
        self.publishing = publishing

    def __str__(self):
        return "name:%s,price:%s,publishing:%s" % (self.name, self.price, self.publishing)


list_book = [
    BookModel("Python", 56.0, "铁道部出版社"),
    BookModel("Java", 47.0, "清华大学出版社"),
    BookModel("C++", 66.0, "清华大学出版社"),
    BookModel("C", 32.0, "铁道出版社"),
    BookModel("JavaScript", 40.0, "清华大学出版社"),
]


# 2.1获取列表中所有图书的名称
print(list(map(lambda b: b.name, list_book)))
for item in map(lambda b: b.name, list_book):
    print(item)
# 2.2获取列表中价格大于50元的图书
for item in filter(lambda e:e.price > 50,list_book):
    print(item)
# 2.3获取名称为“JavaScript”的图书
# for item in filter(lambda e:e.name == "JavaScript",list_book):
#     print(item)
print(IterableHelper.find_single(list_book, lambda e: e.name == "JavaScript"))


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
    RestaurantModel("南京饭店", 2, "南京", 121),
    RestaurantModel("苏州饭店", 0, "苏州", 96),
    RestaurantModel("广州饭店", 6, "广州", 100),
]
#       2.4获取列表中所有餐厅的名称与人均消费
print(list(map(lambda item: (item.name, item.money), list_restaurant)))

#       2.5获取列表中点评人数不为0的餐厅
for item in filter(lambda item:item.remark != 0,list_restaurant):
    print(item)

#       2.6获取名称为“上海饭店”的餐厅
print(IterableHelper.find_single(list_restaurant, lambda item: item.name == "上海饭店"))
