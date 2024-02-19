"""
疫情信息管理系统v1
    从终端录入数据，对(地区名、新增人数、现有人数)进行增加、查询
"""
info_table = [
    {'region': '北京', 'new_pop': 10, 'now_pop': 100},
    {'region': '上海', 'new_pop': 5, 'now_pop': 300}
]
while True:
    print("输入数字1进行增加")
    print("输入数字2显示所有信息")
    print("输入数字3查找指定地区信息")
    print("输入数字4删除指定地区信息")
    print("输入数字0停止")
    number = int(input("请输入数字："))
    if number == 0:
        break
    elif number == 1:
        new_info = {
            "region": input("请输入地区名："),
            "new_pop": int(input("请输入新增人数")),
            "now_pop": int(input("请输入现有人数"))
        }
        info_table.append(new_info)
    elif number == 2:
        for item in info_table:
            print("%s的新增人数为%s，现有人数为%s"%(item['region'], item['new_pop'], item['now_pop']))
    elif number in (3 , 4):
        region = input("请输入指定地区：")
        flag = 0
        for index in range(len(info_table)):
            if info_table[index]['region'] == region:
                if number == 3:
                    print("%s的新增人数为%s，现有人数为%s" % (info_table[index]['region'], info_table[index]['new_pop'], info_table[index]['now_pop']))
                    flag = 1
                if number == 4:
                    print("%s地区的信息已删除"%(region))
                    del info_table[index]
                    flag = 1
                break
        if flag == 0:
            print("您指定的地区不存在！")



