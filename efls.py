"""
厄斐琉斯打假人
"""


class Weapon():
    def __init__(self, name):
        self.count = 50
        self.name = name

    def attack(self):
        self.count -= 1
        print("使用%s进行普攻，消耗弹药1，剩余弹药%s" % (self.name, self.count))

    def q(self):
        self.count -= 10
        print("使用%s释放Q技能，消耗弹药10，剩余弹药%s" % (self.name, self.count))





# weapon_list = [green, red, purple, blue, white]
def switch(list_name, index01=0, index02=1):
    list_name[index01], list_name[index02] = list_name[index02], list_name[index01]


class Weapons():
    def __init__(self,seq=[]):
        self.sequence = seq

    def w(self):
        switch(self.sequence, 0, 1)
        print("切换了主副手武器")

    def check(self):
        print("当前主手武器为%s，剩余弹药%s，副手武器为%s，剩余弹药%s" % (
            self.sequence[0].name, self.sequence[0].count, self.sequence[1].name, self.sequence[1].count))

    def check_count(self):
        if self.sequence[0].count <= 0:
            print("%s弹药消耗完毕，切换为%s" % (self.sequence[0].name, self.sequence[2].name))
            switch(self.sequence, 0, 2)
            self.sequence.append(self.sequence.pop(2))
            self.sequence[4].count = 50


class Aphelios():
    def __init__(self):
        self.green = Weapon("绿刀")
        self.red = Weapon("红刀")
        self.purple = Weapon("紫刀")
        self.blue = Weapon("蓝刀")
        self.white = Weapon("白刀")
        self.weapons = Weapons([self.green,self.red,self.purple,self.blue,self.white])
    def attack(self):
        self.weapons.sequence[0].attack()
        self.weapons.check_count()

    def q(self):
        self.weapons.sequence[0].q()
        self.weapons.check_count()

    def w(self):
        self.weapons.w()
        self.weapons.check()


cyy = Aphelios()
while True:
    get_order = input("请输入操作(a/w/q)")
    if get_order == "a":
        cyy.attack()
    elif get_order == "w":
        cyy.w()
    elif get_order == "q":
        cyy.q()
    elif get_order == "b":
        print("你掉线了！")
        break
    elif get_order == "r":
        print("你释放了大招，酷毙了！")
    elif get_order == "c":
        cyy.weapons.check()
