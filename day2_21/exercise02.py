class Epidemic:
    def __init__(self, name, new=1):
        self.name = name
        self.new = new


bj = Epidemic("北京")
sh = bj
sh.new = 2
print(bj.new)
