# a = {1, 2, 3, 4, 5}
# print(type({}))
#
# print('b' in {"a": "b", "c": "d"}.values())
# print(bool(0))
#
# z = 2
# x = (y := (z + 1))
# print(x)

# a = [1, 2, 3]
# print(id(a))
# b = [3, 4, 5]

# a.extend(b)
# print(a)
# print(id(a)) # 地址相同

# a += b
# print(a)
# print(id(a)) # 地址相同

# a = a + b
# print(a)
# print(id(a)) # 地址不同


# A1 = {"XM":60,"XH":70,"XG":80}
# A2 = {"XG":80,"XM":60,"XH":70}
# print(A1 == A2)
# print(A1 is A2)

# data01 = [10]
# data02 = [10]
#
# print(id(data01[0]) )
# print(id(data02[0]) )

# 19.
# v = dict.fromkeys(["k1","k2","k3"],[])# 只有一个列表
# v["k1"].append(666)
# print(v)
# v["k1"] = 777
# print(v)

# 21.
import copy
a = [1,2,3,4,["a","b"]]
b = copy.copy(a)
c = copy.deepcopy(a)
print(id(a[0])!=id(b[0])!=id(c[0]))
a = 2
b = 2
c = 2
print((a == b) == c)

gene_a = range(10)
print(gene_a.__next__())
AA = gene_a.__iter__()
BB = AA.__iter__()
CC = AA.__iter__()
print(BB is CC)
# range类是一个可迭代对象，而非生成器，成员包括起、止、步长
# 它的__iter__()返回的迭代器对象是一个生成器,拥有指向自身的__iter__()和__next__()方法












