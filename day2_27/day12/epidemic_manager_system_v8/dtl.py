class EpidemicModel:
    def __init__(self, name, new, now):
        self.name = name
        self.new = new
        self.now = now

    def __str__(self):
        return f"{self.name} 新增{self.new} 现有{self.now}"

    def __eq__(self, other):
        return self.name == other
