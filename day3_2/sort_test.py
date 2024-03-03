import random
from common.iterable_tools import IterableHelper as I

list_random = [random.randint(0, 100) for i in range(10)]
print(list_random)


def selection_sort(iterable):
    n = len(iterable)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if iterable[j] < iterable[min_index]:
                min_index = j
        iterable[i], iterable[min_index] = iterable[min_index], iterable[i]
        print(iterable)


selection_sort(list_random)
