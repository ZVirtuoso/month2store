class Epidemic:
    def __init__(self, name, new=1):
        self.name = name
        self.new = new

def func01(p1,p2):
    p1.new=2
    p2 = Epidemic("上海",2)
    print(sh.name is p2.name)

bj = Epidemic("北京")
sh = Epidemic("上海")
print(bj.new is sh.new)
func01(bj,sh)


