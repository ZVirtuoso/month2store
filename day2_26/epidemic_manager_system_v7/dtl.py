class EpidemicModel:
    def __init__(self, name, new=1, now=0):
        self.name = name
        self.new = new
        self.now = now

    def __str__(self):
        return f"{self.name}地区新增人数:{self.new},现有人数:{self.now}"

    def __eq__(self, other):
        return self.name == other.name
