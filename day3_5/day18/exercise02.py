"""
    练习：创建疫情对象列表,写入到文件中,读取会内存依然成为疫情列表
"""


class EpidemicModel:
    def __init__(self, name, new, now):
        self.name = name
        self.new = new
        self.now = now

    def __repr__(self):
        return 'EpidemicModel("%s", %s, %s)'%(self.name, self.new, self.now)

list_epidemic = [
    EpidemicModel("2019-nCoV", 1000000, 100000),
    EpidemicModel("SARS", 1000000, 100000),
    EpidemicModel("H1N1", 1000000, 100000),
    EpidemicModel("MERS", 1000000, 100000),
]

with open("data.txt", "w", encoding="utf-8") as file:
    # 因为列表的__repr__内部会调用元素的__repr__,所以在Model类中重写__repr__
    file.write(list_epidemic.__repr__())

with open("data.txt", "r", encoding="utf-8") as file:
    # 因为列表的__repr__内部会调用元素的__repr__,所以在Model类中重写__repr__
    list_new = eval(file.read()) # type:list[EpidemicModel]
    print(list_new[0].name)
















