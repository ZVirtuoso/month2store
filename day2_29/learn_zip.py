list_name = ['张三', '李四', '王五']
list_long_name = ['张三丰', '李元芳', '王八蛋']
list_room = ['101', '102', '103']
list_big_room = ['1001', '1002', '1003']
# for item in zip(list_name, list_room):
#     print(item)

dict01 = dict(zip(list_name, list_room))
dict02 = dict(zip(list_big_room, list_long_name))
print(dict01)
print(dict02)
# for item in zip(dict01,dict02):
#     print(item)
res = [list(item) for item in zip(dict01,dict02)]
print(res)