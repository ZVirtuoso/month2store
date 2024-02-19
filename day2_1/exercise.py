tuple_number = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tuple_number += (10, 11, 12)
print(tuple_number)
# tuple_number[0] = 666
print(tuple_number)

name = "张无忌"
names = ["赵敏", "周芷若"]
tuple01 = ("张翠山", name, names)
print(tuple01)  # ?
name = "无忌哥哥"
tuple01[2].append("敏儿")
print(tuple01)  # ?
