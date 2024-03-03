class IterableHelper:

    @staticmethod
    def find_single(iterable, condition):
        for item in iterable:
            if condition(item):
                return item

    @staticmethod
    def find_all(iterable, condition):
        for item in iterable:
            if condition(item):
                yield item

    @staticmethod
    def sum(object_iterable, chose_member):
        """
            可迭代对象内元素处理后求和
        :param object_iterable:可迭代对象
        :param chose_member:返回对象处理结果的函数
        """
        summary = 0
        for item in object_iterable:
            summary += chose_member(item)
        return summary

    @staticmethod
    def select_all(object_iterable, chose_member):
        """
            生成可迭代对象内所有对象处理结果

        :param object_iterable:可迭代对象
        :param chose_member:返回对象处理结果的函数
        """
        for item in object_iterable:
            yield chose_member(item)

    @staticmethod
    def delete_single(object_iterable, condition):
        """
            删除可迭代对象内单个满足条件的元素

            参数
            ----------
            object_iterable:可迭代对象
            condition:判断删除条件的函数

            返回
            ----------
            True:删除成功
            False:删除失败
        """
        for i, item in enumerate(object_iterable):
            if condition(item):
                del object_iterable[i]
                return True
        return False

    @staticmethod
    def print_generator(generator):
        """
            for item in generator:
                print(item)
        """
        try:
            for item in generator:
                print(item)
        except TypeError:
            print(generator)

    @staticmethod
    def delete_all(iterable, condition):
        """
            删除可迭代对象内所有满足条件的元素

            iterable:
            condition:
        """
        for i in range(len(iterable) - 1, -1, -1):
            if condition(iterable[i]):
                del iterable[i]

    @staticmethod
    def get_max(iterable, handler):
        """
            获取可迭代对象处理过后的最大值
            可迭代对象包括生成器
            传入空可迭代对象比如[]会raise StopIteration

            max_value获取第一个元素
            后续比较循环从第二个元素开始
        """
        """
            for限用于默认容器和生成器，他们的__iter__()返回的迭代器对象仍是可迭代对象
            但对自定义可迭代对象不适用for，只能从第一个开始比较

            使用while可以避免这一问题，对三类可迭代对象均适用，且均从第二个目标开始比较。
        """
        iterator = iterable.__iter__()
        max_value = iterator.__next__()
        while True:
            try:
                item = iterator.__next__()
                if handler(item) > handler(max_value):
                    max_value = item
            except StopIteration:
                break
        return max_value

    @staticmethod
    def get_min(iterable, handler):
        """
            获取可迭代对象处理过后的最小值
            可迭代对象包括生成器
            传入空可迭代对象比如[]会raise StopIteration

            max_value获取第一个元素
            后续比较循环从第二个元素开始
        """
        """
            for限用于默认容器和生成器，他们的__iter__()返回的迭代器对象仍是可迭代对象
            但对自定义可迭代对象不适用for，只能从第一个开始比较

            使用while可以避免这一问题，对三类可迭代对象均适用，且均从第二个目标开始比较。
        """
        iterator = iterable.__iter__()
        min_value = iterator.__next__()
        while True:
            try:
                item = iterator.__next__()
                if handler(item) < handler(min_value):
                    min_value = item
            except StopIteration:
                break
        return min_value

    @staticmethod
    def ascending_order(iterable, handler):
        """
            对可迭代对象进行升序排序
        """
        # new_iterable = isinstance(iterable)()
        # while True:
        #     iterable_t.__dict__() = iterable.__dict__
