multiplier = lambda x, y: x * y
print(multiplier(3, 4))

# 32.[0,1,4]

# 33.
tuple_database = (("张三", 22, "男"), ("李四", 26, "女"))
print([dict(zip(("name", "age", "sex"), person)) for person in tuple_database])
print(list(map(lambda person: dict(zip(("name", "age", "sex"), person)), tuple_database)))


def fibonacci_sequence(length: int) -> list:
    """
        斐波那契数列
    """
    result = [0, 1]
    if length <= 2: return result
    for i in range(2, length):
        result.append(result[i - 1] + result[i - 2])
    return result


print(fibonacci_sequence(15))

# 34.
list_number = [1, 2, 3, 4, 5]
print([i for i in map(lambda x: x ** 2, list_number) if i > 10])

# 35.
dic = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
print({key: dic[key] for key in sorted(set(dic))})
print(sorted(dic.items()) == sorted(dic.items(),key = lambda item:item[0]))


# 37.
def get_max(iterable, number, handler):
    max_value = iterable[0]
    min_value = iterable[0]
    for i in range(1, number):
        if handler(iterable[i]) > handler(max_value): max_value = iterable[i]
        if handler(iterable[i]) < handler(min_value): min_value = iterable[i]
    return max_value, min_value
