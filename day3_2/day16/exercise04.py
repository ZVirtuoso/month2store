"""
练习：

-- 在商品列表，获取所有名称与单价

-- 在商品列表中，获取所有单价小于10000的商品

-- 对商品列表，根据单价进行降序排列

-- 获取元组中长度最大的列表  ([1,1],[2,2,2],[3,3,3])
"""


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]

# -- 在商品列表，获取所有名称与单价
for item in map(lambda item: (item.name, item.price), list_commodity_infos):
    print(item)
# -- 在商品列表中，获取所有单价小于10000的商品
filterd_list = list(filter(lambda item: item.price < 10000, list_commodity_infos))
print(filterd_list)
# -- 对商品列表，根据单价进行降序排列
list_commodity_infos.sort(key=lambda item: item.price, reverse=True)
print(list_commodity_infos)
# -- 获取元组中长度最大的列表  ([1,1],[2,2,2],[3,3,3])
print(max(([1, 1], [2, 2, 2], [3, 3, 3]), key=lambda item: len(item)))