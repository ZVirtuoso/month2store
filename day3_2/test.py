import copy

from iterable_tools import IterableHelper as I


class Iterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return Iterator(self.data)


class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __next__(self):
        if self.index < len(self.data) - 1:
            self.index += 1
            return self.data[self.index]
        else:
            raise StopIteration


list_nums = [5,1, 2, 7,3, 4, 5]
# iterator = Iterable(list_nums).__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break


# iterable = Iterable(list_nums) # <class 'AttributeError'>
iterable = Iterable(list_nums) #不报错
# iterable = I.find_all(list_nums, lambda x: x > 2) # 不报错

# try:
#     iterable.__iter__().__iter__()
#     iterator = iterable.__iter__()
# except AttributeError:  # 说明iterable是自定义可迭代对象
#     iterator = iterable
#
# for num in iterator:
#     print(num)

# I.print_generator(I.find_all([], lambda x: x))
# print(I.get_max(I.find_all([], lambda x: x % 2 == 0), lambda x: x))
# for i,item in enumerate(I.find_all(list_nums,lambda x:x>2)):
#     print(i,item)

# try:
#     iterable.__iter__().__iter__()
# except Exception as e:
#     print(type(e))
# else:
#     try:
#         iterable.__next__()
#     except Exception as e:
#         print(type(e))
#     pass

print(isinstance(range(10),object))
