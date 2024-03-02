"""
    2.创建函数,获取列表中所有大于等于25的年龄
      创建函数,获取列表中第一个大于等于25的年龄
      list_age = [26,23,20,28,24]
    3.创建函数,获取列表中所有三个字的姓名
      创建函数,获取列表中第一个三个字的姓名
      list_name = ["悟空","猪八戒","唐三藏","沙僧","小白龙"]
"""
list_age = [26, 23, 20, 28, 24]
list_name = ["悟空", "猪八戒", "唐三藏", "沙僧", "小白龙"]

def get_ages_gt_25():
    for item in list_age:
        if item >= 25:
            yield item

def get_age_gt_25():
    for item in list_age:
        if item >= 25:
            return item

def get_names_len_3():
    for item in list_name:
        if len(item) == 3:
            yield item

def get_name_len_3():
    for item in list_name:
        if len(item) == 3:
            return item
            
# for 生成器可以节省内存
for item in get_ages_gt_25():
    print(item)

# 将生成器转换为容器,可以发挥容器(增删改查)优势
list_result  = list(get_names_len_3())
print(list_result[-1])


