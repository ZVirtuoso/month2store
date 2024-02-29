import random

number_list = random.sample(range(100), k=random.randint(1, 15))
print(number_list)
for i, item in enumerate(number_list):
    if item % 2 == 1:
        number_list[i] = None
    else:
        number_list[i] += 1
print(number_list)
