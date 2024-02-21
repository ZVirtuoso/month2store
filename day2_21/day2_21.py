class Epidemic:
    def __init__(self,name,new,now):
        self.name = name
        self.new = new
        self.now = now

    def display(self):
        print("%s地区的新增人数是%s,现有人数是%s" % (self.name, self.new, self.now))

bj = Epidemic("北京",1,2)
print(bj.name)
bj.display()

sh = Epidemic("上海",2,3)
print(sh.name)
sh.display()
