"""
    数据的存储和读取,使用__repr__重构函数
"""


class EpidemicModel:
    def __init__(self, city: str, new: int, now: int):
        self.city = city
        self.new = new
        self.now = now

    def __str__(self):
        return f"{self.city}城市新增{self.new},现有{self.now}"

    def __repr__(self):
        return f'EpidemicModel("{self.city}", {self.new}, {self.now})'


# 1.内存中的对象
list_epidemic = [
    EpidemicModel("北京", 2, 300),
    EpidemicModel("上海", 5, 500),
    EpidemicModel("天津", 7, 230),
    EpidemicModel("重庆", 1, 137),
]

# 2.写入到文件中
with open("./data.txt", "w", encoding="utf-8") as file:
    for model in list_epidemic:
        file.write(model.__repr__() + "\n")

# 3.读取文件
list_new = []  # type: list[EpidemicModel]
with open("./data.txt", "r", encoding="utf-8") as file:
    # print(file.read()+"555")
    # print(file.read()+"666")
    for line in file.readlines():
        list_new.append(eval(line))

for item in list_new:
    print(item.__str__())
