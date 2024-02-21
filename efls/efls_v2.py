"""
厄斐琉斯打假人v2
副武器不参与轮换，单独做一个变量，剩余武器做轮换


"""
import random

attack_voice = (
    '"月石的裁断！"',
    '"由命运牵动的武器！"',
    '"我在这里，也能听见你战斗的回响！"',
    '"生自黑夜！"',
    '"现身之人，无往不利！"',
    '"归于寂静！"',
    '"你是世人眼中的月蚀！"',
    '"一念一动，天人永隔！"',
    '"伸出手来，厄斐琉斯！"',
    '"月光之力！"'
    '"随遇而动！"'
    '"月有阴晴，七形轮转！"'
    '"直至黑夜长留！"'
    '"我们将不再遮掩！"'
    '"信念，与你同行！"'
    '"黑夜，许你长眠！"'
    '"他们，向着死亡而环绕！"'
    '"我为你，带去光芒！"'
    '"月石与精魂，尽数归于手中！"'
    '"皎月赐福！"'
    '"出自你手，发自我心！"'
    '"这就是你的话音！"'
    '"信仰的力量！"'
    '"厄斐琉斯，你要相信！"'
    '"他们必将，以血还血！"'
    '"他们的命运，紧握在你手中！"'
    '"灵与力的融汇！"'
    '"愿他们的灵魂，在抽离黑夜之后，得以安息！"'
    '"哥哥，向死求生，宿命使然！"'
    '"你焕发光芒，月亮便相形失色，厄斐琉斯，你做的很好！"'
    '"他们只是月光中盈盈浮动的尘埃！"'
    '"月之母，请接引他们！"'
    '"皎月赐福！"'
)
def battlecry(attack_count):
    if attack_count % 3 == 0 :
        print(random.choice(attack_voice))
# WEAPONS = ("绿刀","红刀","紫刀","蓝刀","白刀")
class Aphelios():
    def __init__(self):
        self.pri_count = 50
        self.sec_count = 50
        self.weapons = ["绿刀", "紫刀", "蓝刀", "白刀"]
        self.sec_weapon = "红刀"
        self.green_mark = False
        self.purple_mark = False
        self.white_num = 0
        self.attack_count = 0
        print('"厄斐琉斯，千万利器，莫过于你的信念！"')

    def use_green_mark(self):
        if self.green_mark:
            if self.white_num > 0:
                print("%s个小飞轮一同攻击了敌人" % (self.white_num))
            if self.sec_weapon == '绿刀':
                print("使用%s特殊攻击了带有绿刀标记的敌人" % (self.weapons[0]))
                self.special_a(self.weapons[0])
            else:
                print("使用%s特殊攻击了带有绿刀标记的敌人" % (self.sec_weapon))
                self.special_a(self.sec_weapon)

            self.green_mark = False

    def special_a(self, weapon):
        if weapon == "绿刀":
            print("绿刀攻击标记了敌人")
            self.green_mark = True
            self.use_green_mark()
        if weapon == "红刀":
            print("红刀攻击回血了")
        if weapon == "紫刀":
            print("紫刀攻击使敌人减速了")
            self.purple_mark = True
        if weapon == "蓝刀":
            print("造成了大量AOE伤害")
        if weapon == "白刀":
            self.white_num += 1
            print("飞轮增加了到了%s个" % (self.white_num))

    def check(self):
        print("当前主武器为%s，剩余弹药%s；副武器为%s，剩余弹药%s" % (
            self.weapons[0], self.pri_count, self.sec_weapon, self.sec_count))

    def switch(self):
        self.weapons[0], self.sec_weapon = self.sec_weapon, self.weapons[0]
        self.pri_count, self.sec_count = self.sec_count, self.pri_count
        self.check()

    def check_out(self):
        if self.pri_count <= 0:
            if self.weapons[0] == "白刀":
                self.white_num = 0
            """"""
            self.weapons = self.weapons[1:] + self.weapons[:1]
            if self.weapons[0] == "绿刀": print(
                random.choice(['"通碧！"', '"满月尽照！"', '"哥哥，远方的敌人也不要放过！"', '"月光所指，一击即中！"']))
            if self.weapons[0] == "红刀": print(
                random.choice(['"断魄！"', '"残月抱影！"', '"刈除杂草，才有新生！"', '"收取死亡，是为了滋养生命！"']))
            if self.weapons[0] == "紫刀": print(
                random.choice(['"坠明！"', '"新月暗初！"', '"无人可以逃脱！"', '"黑暗中，人人踉跄！"', '"黑暗，不可背负之重！"']))
            if self.weapons[0] == "蓝刀": print(
                random.choice(['"莹焰！"', '"月火渐盛！"', '"启明众生！"', '"星火，燃透夜空！"']))
            if self.weapons[0] == "白刀":
                print(random.choice(['"折镜！"', '"对镜成圆！"', '"飞刃向心！"', '"死亡之弧，由你手中划出！"']))
            self.pri_count = 50
            print("%s子弹消耗完毕，主武器切换为%s" % (self.weapons[3], self.weapons[0]))

        self.check()

    def attack(self):
        self.attack_count += 1
        battlecry(self.attack_count)
        self.pri_count -= 1
        print("使用%s进行普通攻击，消耗1弹药" % (self.weapons[0]))
        if self.weapons[0] == "紫刀":
            self.purple_mark = True
        if self.weapons[0] == "白刀":
            if self.white_num > 0:
                print("%s个小飞轮一同攻击了敌人" % (self.white_num))
        self.check_out()

    def q_skill(self):
        if (self.weapons[0] == "紫刀") & (self.purple_mark == False):
            print("没有被紫刀标记的敌人")
            return None
        self.attack_count += 1
        battlecry(self.attack_count)
        if (self.weapons[0] == "紫刀") & (self.purple_mark == True):
            self.purple_mark = False
        self.pri_count -= 10
        print("使用%s释放Q技能，消耗10弹药" % (self.weapons[0]))
        if self.weapons[0] == "绿刀":
            print("妹妹发把狙！超远距离标记了敌人")
            self.check_out()
            self.green_mark = True
            self.use_green_mark()
        elif self.weapons[0] == "红刀":
            print("交替使用红刀和%s攻击了敌人，并触发了%s的特殊攻击" % (self.sec_weapon, self.sec_weapon))
            self.check_out()  # 红绿刀，红刀用完，绿刀的标记由新的主武器触发
            if self.sec_weapon != "绿刀":
                self.special_a(self.sec_weapon)
                self.special_a(self.sec_weapon)
                self.special_a(self.sec_weapon)
                self.special_a(self.sec_weapon)
            else:
                self.special_a(self.sec_weapon)

        elif self.weapons[0] == "紫刀":
            print("使用紫刀禁锢了敌人！")
            self.check_out()
        elif self.weapons[0] == "蓝刀":
            print("使用蓝刀攻击了成片的敌人，并使用%s再次攻击了他们" % (self.sec_weapon))
            self.check_out()  # 蓝绿刀，蓝刀用完，绿刀的标记由新的主武器触发
            self.special_a(self.sec_weapon)
        elif self.weapons[0] == "白刀":
            print("释放地灵持续使用%s攻击敌人" % self.sec_weapon)
            self.check_out()  # 白绿刀，白刀用完，绿刀的标记由新的主武器触发
            self.special_a(self.sec_weapon)
            self.special_a(self.sec_weapon)
            self.special_a(self.sec_weapon)

    def r_skil(self):
        print('"我与你同在！"')
        if self.weapons[0] == "白刀":
            print("清辉夜凝攻击为你增加了五个飞轮！")
            self.white_num += 5
            print("飞轮增加到了%s个" % (self.white_num))
        if self.weapons[0] == "紫刀":
            print("清辉夜凝攻击并减速了敌人！")
            self.purple_mark = True
        if self.weapons[0] == "绿刀":
            print("清辉夜凝攻击标记了敌人！")
            self.green_mark = True
            self.use_green_mark()
        if self.weapons[0] == "蓝刀":
            print("清辉夜凝攻击了敌人，并放了个大烟花！")
        if self.weapons[0] == "红刀":
            print("清辉夜凝攻击了敌人，并恢复了你的生命值！")


cyy = Aphelios()
while True:
    get_order = input("请输入操作(a/w/q/r)")
    if get_order == "a":
        cyy.attack()
    elif get_order == "w":
        cyy.switch()
    elif get_order == "q":
        cyy.q_skill()
    elif get_order == "b":
        if input("你掉线了！输入'quit'结束") == 'quit':
            break
        else:
            print("你已重新连接")
    elif get_order == "r":
        cyy.r_skil()
    elif get_order == "c":
        cyy.check()
