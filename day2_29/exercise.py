list_number = [43, 43, 54, 56, 76, 87, 98]
list_chaos = [43, '悟空', True, 56, '八戒', 87.5, 98]


def get_even_numbers(list_name):
    for number in list_name:
        if number % 2 == 0:
            yield number


def get_number_from_list(list_name):
    for chaos_item in list_name:
        # if type(chaos_item) in (int, float): # 更好的选择
        if isinstance(chaos_item, (int, float)) and not isinstance(chaos_item, bool):
            yield chaos_item


# for number in get_even_numbers(list_number):
#     print(number)

for item in get_number_from_list(list_chaos):
    print(item)
# print(isinstance(False,int))
# True False bool是int类型的子类，但type()的结果不同
# print(type(True) == bool) #False
