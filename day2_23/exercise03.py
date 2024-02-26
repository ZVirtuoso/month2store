"""
重构内置函数，疫情练习
+   相加之后返回新对象
+=  对于可变数据，应该修改数据本身
    对于不可变数据，创建新的数据并返回
"""


class EpidemicModel:
    def __init__(self, name, new=1, now=0):
        self.name = name
        self.new = new
        self.now = now

    def __str__(self):
        return f'{self.name}地区新增案例{self.new},现有案例 {self.now}'

    # 相加：返回新对象
    def __add__(self, other):
        if type(other) is EpidemicModel:
            if self.name == other.name:
                return EpidemicModel(name=self.name,
                                     new=other.new,
                                     now=self.now + other.new + other.now)
            return EpidemicModel(name=self.name + "和" + other.name,
                                 new=self.new + other.new,
                                 now=self.now + other.now)
        if type(other) is int:
            return EpidemicModel(name=self.name, new=other, now=self.now + self.new)

    # 累加：返回原对象
    def __iadd__(self, other):
        self.name += other.name
        self.now += other.now
        self.new += other.new
        return self


ep1 = EpidemicModel("北京", 1, 10)
ep2 = EpidemicModel("北京", 2, 10)
# print(ep1+ep2)
# ep3 = EpidemicModel("上海",5,100)
# print(ep1 + ep3)
print(id(ep1))  # id()为查询变量指向的数据在内存中的地址
ep1 += ep2
print(ep1)
print(id(ep1))
