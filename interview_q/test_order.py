from iterable_tools import IterableHelper as I

number_list = [243, 256, 343, 74, 55, 65, 72, 83, 91, 1010]
number_generator = I.find_all(number_list, lambda n: n % 3 == 0)
print(I.ascending_order(number_generator, reverse=True))

a = [("a", 3), ("b", 2), ("d", 0)]
print(sorted(a, key=lambda x: x[1]))

s = "k:1|k1:2|k3:4|k4:5|k5:3"
print(dict(item.split(":") for item in s.split("|")))
