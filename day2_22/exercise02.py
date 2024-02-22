"""
玩家攻击敌人,敌人受伤(头顶爆字).
"""


class Player:
    def __init__(self, name, atk):
        self.name = name
        self.atk = atk
        self.health = 100

    def attack(self, enemy):
        print(self.name + "攻击了" + enemy.name+"，造成%s的伤害"%self.atk)
        enemy.be_attacked(self)

    def be_attacked(self,enemy):
        self.health -= enemy.atk
        print(self.name + "被攻击了,剩余生命值%s"%self.health)


yasuo = Player("yasuo",10)
yone = Player("yone",15)
yasuo.attack(yone)
