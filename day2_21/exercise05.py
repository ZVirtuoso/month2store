class Epidemic:
    def __init__(self, name, new=1):
        self.name = name
        self.new = new


def get_names(list_data):
    list_name = []
    for item in list_data:
        list_name.append(item.name)
    return list_name


list_table = [
    Epidemic("北京",6),
    Epidemic("上海", 6)
]
res = get_names(list_table)
print(res)