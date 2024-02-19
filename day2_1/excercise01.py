"""

"""
# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = ["北京",list]
# list[2] = list2
# print(list)
# print(list2)
#
# list_region = ["台湾","陕西","浙江"]
# data01 = list_region
# data02 = list_region[-2:]
# data02[0] = "shan_xi"
# print(list_region)
# data01[0] = "tai_wan"
# print(list_region)

list_region = ["台湾", "陕西", "浙江"]
list_new = [16, 182, 2]
list_now = [2339, 859, 505]
for item in list_new:
    if item < 10:
        print(item)
for i in range(len(list_now)):
    list_now[i] +=2
print(list_new)
print(list_now)

last_region = list_region.pop(1)
print(list_region)
print(last_region)
