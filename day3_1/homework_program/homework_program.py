from iterable_tools import IterableHelper

# if __name__ == "__main__":
#     # 2. 使用IterableHelper类实现下列功能：
#     #         2.1获取列表中所有图书的名称
#     #         2.2获取列表中价格大于50元的图书
#     #         2.3删除列表中图书名"Python"的图书
#     #         2.4累加所有图书价格
#     #         2.5获取名称为“JavaScript”的图书
#     class BookModel:
#         def __init__(self, name="", price=0.0, publishing=""):
#             self.name = name
#             self.price = price
#             self.publishing = publishing
#
#         def __str__(self):
#             return f"Name: {self.name}, Price: {self.price}, Publishing: {self.publishing}"
#
#
#     list_book = [
#         BookModel("Python", 56.0, "铁道部出版社"),
#         BookModel("Java", 47.0, "清华大学出版社"),
#         BookModel("C++", 66.0, "清华大学出版社"),
#         BookModel("C", 32.0, "铁道出版社"),
#         BookModel("JavaScript", 40.0, "清华大学出版社"),
#     ]
#     # 2.1
#     print(list(IterableHelper.select_all(list_book, lambda x: x.name)))
#
#     # 2.2
#     for book in IterableHelper.find_all(list_book, lambda x: x.price > 50):
#         print(book)
#
#     # 2.3
#     print(IterableHelper.delete_sigle(list_book, lambda x: x.name == "Python"))
#     # print(*list_book, sep='\n')  # 查询删除后列表内容
#
#     # 2.4
#     print(IterableHelper.sum(list_book, lambda x: x.price))
#
#     # 2.5
#     print(IterableHelper.find_single(list_book, lambda x: x.name == "JavaScript"))

if __name__ == "__main__":
    class RestaurantModel:  # 餐厅
        def __init__(self, name="", remark=0, city="北京", money=0.0):
            self.name = name
            self.remark = remark
            self.city = city
            self.money = money

        def __str__(self):
            return f"餐厅名称：{self.name}, 点评人数：{self.remark}, 城市：{self.city}, 人均消费：{self.money}"


    list_restaurant = [
        RestaurantModel("北京饭店", 4, "北京", 132),
        RestaurantModel("上海饭店", 3, "上海", 142),
        RestaurantModel("南京饭店", 2, "南京", 121),
        RestaurantModel("苏州饭店", 0, "苏州", 96),
        RestaurantModel("广州饭店", 6, "广州", 100),
    ]
    # 2.6
    # 获取列表中所有餐厅的名称与人均消费
    for item in IterableHelper.select_all(list_restaurant, lambda x: f"餐厅名称：{x.name}, 人均消费：{x.money}"):
        print(item)
    # 2.7
    # 删除列表中
    # "广州饭店"
    print(IterableHelper.delete_single(list_restaurant, lambda x: x.name == "广州饭店"))
    # 2.8
    # 累加所有餐厅的人均消费
    print(IterableHelper.sum(list_restaurant, lambda x: x.money))
    # 2.9
    # 获取列表中点评人数不为0的餐厅
    # for item in IterableHelper.find_all(list_restaurant, lambda x: x.remark != 0):
    #     print(item)
    IterableHelper.print_generator(IterableHelper.find_all(list_restaurant, lambda x: x.remark != 0))
    # 2.10
    # 获取名称为“上海饭店”的餐厅
    print(IterableHelper.find_single(list_restaurant, lambda x: x.name == "上海饭店"))

    # IterableHelper.print_generator(IterableHelper.find_all(range(100), lambda x: x % 11 == 0 and x != 0 and x % 2 == 0))
