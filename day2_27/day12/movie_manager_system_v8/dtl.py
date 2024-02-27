class MovieModel:
    def __init__(self, name="", type=(), actor="", index=0):
        self.name = name
        self.type = type
        self.actor = actor
        self.index = index

    def __str__(self):
        return "%s的类型是%s,主演是%s,指数为%s" % (self.name, "-".join(self.type), self.actor, self.index)

    def __eq__(self, other):
        return self.name == other.name
