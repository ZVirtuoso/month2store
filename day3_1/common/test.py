from iterable_tools import IterableHelper as I

# print(len(I.find_all([5,4,1,6556,4,5465,561,65],lambda x:x%2 == 0)))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# I.delete_all(nums, lambda x: x % 2 == 0)
# print(nums)
generator = (x for x in nums if x % 2 == 0)

I.print_generator(I.find_single(generator, lambda x: x % 3 == 0))
