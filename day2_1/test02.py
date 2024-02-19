"""

"""
# list = list("jfalgknwgaoislz")
# list_a = list[:]  # 浅拷贝，通过切片创建新列表，在处理列表之前留存副本
# list.sort()
# print(list)
# print(list_a)
#
# import copy

# list_movie = ["八角笼中", ["消失的她", "碟中谍7"]]
# list_new = copy.deepcopy(list_movie)  # 深拷贝占内存


# list_exercise01 = [x for x in range(10, 30) if x % 3 == 0 or x % 5 == 0]
# print(list_exercise01)
#
# list_exercise02 = [x ** 2 for x in range(5, 20)]
# print(list_exercise02)


test_list = [(x + "2") * 2 for x in "range(1, 11)" if "a" <= x <= "z"]
print(test_list)

a,b = "12"
print(a,b)
print(a == 1 )


