"""
3.餐厅信息管理系统V4
    定义餐厅模型类(实例变量:名称,城市,点评人数,人均消费)
    定义餐厅视图类
        定义显示菜单函数
        定义选择菜单函数
        定义入口函数
        定义录入餐厅(名称,城市,点评人数,人均消费)函数
        定义查看餐厅(名称,城市,点评人数,人均消费)函数
        定义移除餐厅(名称)函数
        定义更新餐厅(名称,城市,点评人数,人均消费)函数
    定义餐厅控制器类
        定义列表
        定义添加餐厅函数
        定义删除餐厅函数
        定义修改餐厅函数
"""


class RestaurantModel:
    def __init__(self, name, city, number_reviewers, ave_consumption):
        self.name = name
        self.city = city
        self.number_reviewers = number_reviewers
        self.ave_consumption = ave_consumption


class RestaurantView:
    def __init__(self):
        self.controller = RestaurantController()

    def show_menu(self):
        print("输入1录入餐厅")
        print("输入2查看餐厅")
        print("输入3移除餐厅")
        print("输入4更新餐厅")
        print("输入5退出程序")

    def select_menu(self):
        number = input("请输入指令：")
        if number == "1": self.add_restaurant()
        if number == "2": self.check_restaurant()
        if number == "3": self.delete_restaurant()
        if number == "4": self.modify_restaurant()
        if number == "5": exit()

    def add_restaurant(self):
        new_restaurant = RestaurantModel(
            name=input("请输入名字："),
            city=input("请输入城市："),
            number_reviewers=int(input("请输入点评人数：")),
            ave_consumption=float(input("请输入人均消费：")),
        )
        if self.controller.add(new_restaurant): print("添加成功")

    def check_restaurant(self):
        for item in self.controller.restaurants_list:
            print("%s餐厅位于%s城市，点评人数为%s，人均消费%s" % (
                item.name, item.city, item.number_reviewers, item.ave_consumption))

    def delete_restaurant(self):
        name = input("请输入要删除餐厅名字：")
        if self.controller.delete_restaurant(name):
            print("删除成功")
        else:
            print("您输入的餐厅不在列表中")

    def modify_restaurant(self):
        name = input("请输入要修改餐厅名字：")
        new_restaurant = RestaurantModel(
            name=input("请输入新的名字："),
            city=input("请输入新的城市："),
            number_reviewers=int(input("请输入新的点评人数：")),
            ave_consumption=float(input("请输入新的人均消费：")),
        )
        if self.controller.modify_restaurant(name, new_restaurant):
            print("修改成功")
        else:
            print("您输入的餐厅不在列表中")
        pass

    def main(self):
        while True:
            self.show_menu()
            self.select_menu()


class RestaurantController:
    def __init__(self):
        self.restaurants_list = []  # type: list[RestaurantModel]

    def add(self, restaurant):
        self.restaurants_list.append(restaurant)
        return True

    # def is_in_list(self, name):
    #     for item in self.restaurants_list:
    #         if item.name == name:
    #             return True
    #     return False
    def delete_restaurant(self, name):
        for i in range(len(self.restaurants_list)):
            if self.restaurants_list[i].name == name:
                del self.restaurants_list[i]
                return True
        return False

    def modify_restaurant(self, name, new_restaurant):
        for item in self.restaurants_list:
            if item.name == name:
                item.__dict__ = new_restaurant.__dict__
                return True
        return False

view = RestaurantView()
view.main()