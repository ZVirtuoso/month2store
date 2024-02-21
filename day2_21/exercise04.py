class Epidemic:
    def __init__(self, name, new=1):
        self.name = name
        self.new = new


bj = Epidemic("北京")
list_table = [
    bj,
    Epidemic("上海", 6)
]
new_sum = 0
for item in list_table:
    new_sum += item.new
print(new_sum)