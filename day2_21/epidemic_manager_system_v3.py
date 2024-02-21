"""
    疫情信息管理系统V2
"""
list_table = []


def display_menu():
    """显示菜单"""
    print("输入1键录入疫情信息")
    print("输入2键显示疫情信息")
    print("输入3键删除疫情信息")
    print("输入4键修改疫情信息")
    print("输入5键退出程序")

class Epidemic:
    def __init__(self, name="",new = 0, now = 0):
        self.name = name
        self.new = new
        self.now = now
def input_epidemic():
    dict_epidemic = {
        "name": input("请输入疫情名称:"),
        "new": int(input("请输入新增人数:")),
        "now": int(input("请输入现有人数:")),
    }
    list_table.append(dict_epidemic)


def display_epidemic():
    for item in list_table:
        print("%s地区的新增人数是%s,现有人数是%s" % (item["name"], item["new"], item["now"]))


def delete_epidemic():
    name = input("请输入疫情名称:")
    for i in range(len(list_table)):  # 0 1 2
        if list_table[i]["name"] == name:
            del list_table[i]
            break


def modify_epidemic():
    name = input("请输入需要修改的地区名:")
    for item in list_table:
        if item["name"] == name:
            item["new"] = int(input("请输入新增人数:"))
            item["now"] = int(input("请输入现有人数:"))
            break


def select_menu():
    number = input("请输入选项:")
    if number == "1":
        input_epidemic()
    elif number == "2":
        display_epidemic()
    elif number == "3":
        delete_epidemic()
    elif number == "4":
        modify_epidemic()
    elif number == "5":
        exit()


while True:
    display_menu()
    select_menu()
