"""
小明请保洁打扫卫生
"""


class Person:
    def __init__(self, name):
        self.name = name

    def employ(self, worker):
        print(self.name + "雇佣了" + worker.name)
        worker.work()


class Cleaner:
    def __init__(self):
        self.name = "保洁"

    def work(self):
        print("保洁打扫了卫生，真是干干又净净")


xm = Person("小明")
xm.employ(Cleaner())
