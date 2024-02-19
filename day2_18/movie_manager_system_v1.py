"""
电影信息管理系统v1
    从终端录入数据，对电影进行增删改查
    电影名、类型、演员、指数
"""
list_table=[]
while True:
    # 1.显示菜单
    print("输入1键录入电影")
    print("输入2键显示电影")
    print("输入3键删除电影")
    print("输入4键修改电影")
    # 2.选择菜单
    number = input("请输入选项")
    if number == '1':
        dict_movie = {
            "name":input("请输入电影名称"),
            "type":tuple(input("请输入电影类型(-分割)").split("-")),
            "actor":input("请输入电影演员(-分割)"),
            "index":int(input("请输入电影指数"))
        }
        list_table.append(dict_movie)
    elif number == '2':
        for item in list_table:
            print("%s的类型是%s，主演是%s，指数为%s" %(item["name"],'-'.join(item["type"]),item["actor"],item["index"]))
    elif number == '3':
        pass
    elif number == '4':
        pass