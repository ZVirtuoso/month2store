from iterable_tools import IterableHelper as I

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TypeError: object of type 'generator' has no len()
# print(len(I.select_all(nums, lambda x: x % 2 == 0)))

# TypeError: 'generator' object is not subscriptable
print(I.get_min(I.find_all(nums, lambda x: x % 2 == 0),lambda x:x))


map_object = map(lambda x : x+1,nums)